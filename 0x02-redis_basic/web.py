#!/usr/bin/env python3
from datetime import datetime, timedelta
from requests import get

cache = {}
cache_expiration = 10  # Seconds


def access_counter(url):
    cache_key = f"count:{url}"
    if cache_key not in cache:
        cache[cache_key] = 0
    cache[cache_key] += 1


def cache_decorator(func):
    def wrapper(url):
        cache_key = f"{func.__name__}:{url}"
        current_time = datetime.now()
        if (
            cache_key in cache
            and (current_time - cache[cache_key]["time"]).total_seconds()
            < cache_expiration
        ):
            return cache[cache_key]["data"]
        else:
            data = func(url)
            cache[cache_key] = {"data": data, "time": current_time}
            access_counter(url)
            return data

    return wrapper


@cache_decorator
def get_page(url):
    response = get(url)
    return response.text
