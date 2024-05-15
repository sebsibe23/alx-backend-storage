import requests
import redis
from functools import wraps
from typing import Callable

# Initialize Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(url: str) -> str:
        # Check if the result is already cached
        cached_page = r.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode('utf-8')
        
        # Get the page content
        page_content = func(url)
        
        # Cache the result with an expiration time of 10 seconds
        r.setex(f"cached:{url}", 10, page_content)
        
        return page_content
    return wrapper

@cache_page
def get_page(url: str) -> str:
    # Increment the access count for the URL
    r.incr(f"count:{url}")
    
    # Get the HTML content of the URL
    response = requests.get(url)
    response.raise_for_status()
    
    return response.text

# Test the function with a slow response simulation
if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    print(get_page(test_url))
    print(get_page(test_url))  # Should use the cached result
    print(r.get(f"count:{test_url}").decode('utf-8'))  # Should show the number of accesses
