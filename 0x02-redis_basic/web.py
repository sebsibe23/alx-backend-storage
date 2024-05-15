#!/usr/bin/env python3
import requests
from functools import lru_cache

# Create a dictionary to store the count of URL accesses
url_count = {}


@lru_cache(maxsize=32)
def get_page(url: str) -> str:
    # Increase the count of the URL
    url_count[url] = url_count.get(url, 0) + 1

    # Get the HTML content of the URL
    response = requests.get(url)

    # Return the HTML content
    return response.text


# Test the function with a slow URL
url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))
print("URL count:", url_count[url])
