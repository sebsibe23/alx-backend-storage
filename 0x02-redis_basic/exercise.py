#!/usr/bin/env python3
"""A module for using the Redis NoSQL data storage.
"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """
    Tracks the number of calls made to a method in a Cache class.

    Parameters:
    method (Callable): The method to be wrapped and
    have its call count tracked.

    Returns:
    Callable: A new function that wraps the original method
    and tracks its call count.
    """

    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Invokes the given method after incrementing its call counter.

        Parameters:
        self (Any): The instance of the class containing the method.
        *args (Any): Positional arguments to be passed to the original method.
        **kwargs (Any): Keyword arguments to be passed to the original method.

        Returns:
        Any: The return value of the original method.
        """
        try:
            if isinstance(self._redis, redis.Redis):
                self._redis.incr(method.__qualname__)
            return method(self, *args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None

    return invoker


def call_history(method: Callable) -> Callable:
    """
    Tracks the call details of a method in a Cache class.

    Parameters:
    method (Callable): The method to be wrapped
    and have its call history tracked.

    Returns:
    Callable: A new function that wraps the original
    method and tracks its call history.
    """

    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Returns the method's output after storing its inputs and output.

        Parameters:
        self (Any): The instance of the class containing the method.
        *args (Any): Positional arguments to be passed to the original method.
        **kwargs (Any): Keyword arguments to be passed to the original method.

        Returns:
        Any: The return value of the original method.
        """
        try:
            in_key = "{}:inputs".format(method.__qualname__)
            out_key = "{}:outputs".format(method.__qualname__)
            if isinstance(self._redis, redis.Redis):
                self._redis.rpush(in_key, str(args))
            output = method(self, *args, **kwargs)
            if isinstance(self._redis, redis.Redis):
                self._redis.rpush(out_key, str(output))
            return output
        except Exception as e:
            print(f"Error: {e}")
            return None

    return invoker


def replay(fn: Callable) -> None:
    """
    Displays the call history of a Cache class' method.

    Parameters:
    fn (Callable): The method to display the call history for.
    """
    if fn is None or not hasattr(fn, "__self__"):
        return

    redis_store = getattr(fn.__self__, "_redis", None)
    if not isinstance(redis_store, redis.Redis):
        return

    fxn_name = fn.__qualname__
    in_key = "{}:inputs".format(fxn_name)
    out_key = "{}:outputs".format(fxn_name)

    try:
        fxn_call_count = 0
        if redis_store.exists(fxn_name) != 0:
            fxn_call_count = int(redis_store.get(fxn_name))

        print(f"{fxn_name} was called {fxn_call_count} times:")

        fxn_inputs = redis_store.lrange(in_key, 0, -1)
        fxn_outputs = redis_store.lrange(out_key, 0, -1)

        for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
            print(
                f"{fxn_name}(*{fxn_input.decode('utf-8')}) -> {fxn_output.decode('utf-8')}"
            )
    except Exception as e:
        print(f"Error: {e}")


class Cache:
    """Represents an object for storing data in a Redis data storage."""

    def __init__(self) -> None:
        """Initializes a Cache instance."""
        try:
            self._redis = redis.Redis()
            self._redis.flushdb(True)
        except Exception as e:
            print(f"Error: {e}")

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """

           Args:
               data (Union[str, bytes, int, float]): [description]

           Returns:
               str: [description]
        Stores a value in a Redis data storage and returns the key."""
        try:
            data_key = str(uuid.uuid4())
            self._redis.set(data_key, data)
            return data_key
        except Exception as e:
            print(f"Error: {e}")

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """

        Args:
            key (str): [description]
            fn (Callable, optional): [description]. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: [description]

        Retrieves a value from a Redis data storage.
        """
        try:
            data = self._redis.get(key)
            return fn(data) if fn is not None else data
        except Exception as e:
            print(f"Error: {e}")

    def get_str(self, key: str) -> str:
        """_summary_

         Args:
             key (str): _description_

         Returns:
             str: _description_
        Retrieves a string value from a Redis data storage.
        """
        try:
            return self.get(key, lambda x: x.decode("utf-8"))
        except Exception as e:
            print(f"Error: {e}")
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """_summary_

          Args:
              key (str): _description_

          Returns:
              int: _description_
        Retrieves an integer value from a Redis data storage.
        """
        try:
            return self.get(key, lambda x: int(x))
        except Exception as e:
            print(f"Error: {e}")
        return self.get(key, lambda x: int(x))
