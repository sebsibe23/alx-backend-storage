#!/usr/bin/env python3
"""A module with tools for request caching and tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""The module-level Redis instance.
"""


def data_cacher(method: Callable) -> Callable:
    """Caches the output of fetched data."""

    @wraps(method)
    def invoker(url) -> str:
        """

        Args:
            url ([type]): [description]

        Returns:
            str: [description]
        The wrapper function for caching the output.
        """
        try:
            redis_store.incr(f"count:{url}")
            result = redis_store.get(f"result:{url}")
            if result:
                return result.decode("utf-8")
            result = method(url)
            redis_store.set(f"count:{url}", 0)
            redis_store.setex(f"result:{url}", 10, result)
            return result
        except Exception as e:
            print(e)

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        str: _description_
    Returns the content of a URL after caching
    the request's response,
    and tracking the request.
    """
    try:
        return requests.get(url).text
    except Exception as e:
        print(e)
