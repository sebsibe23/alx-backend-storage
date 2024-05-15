0x02. Redis basic
# Redis Basic Operations and Caching with Python

## Introduction

This project provides a comprehensive guide on how to use Redis for basic operations and as a simple cache with Python. The instructions and examples provided are compatible with Ubuntu 18.04 LTS using Python 3.7.

## Resources

To get started with Redis, you can refer to the following resources:

- [Redis Crash Course Tutorial](#)
- [Redis commands](#)
- [Redis python client](#)
- [How to Use Redis With Python](#)

## Learning Objectives

By the end of this project, you will learn:

- How to use Redis for basic operations.
- How to use Redis as a simple cache.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Ensure all files end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Your code should follow the pycodestyle style (version 2.5).
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- Documentation should consist of full sentences explaining the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.

## Installation

### Install Redis on Ubuntu 18.04

To install Redis on your Ubuntu 18.04 system, run the following commands:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Use Redis in a Container

If you are using Redis in a container, note that the Redis server is stopped by default. When starting a container, you should start the Redis server with the following command:

```bash
$ service redis-server start
```

## Usage

### Basic Redis Operations

To perform basic Redis operations using Python, you can use the `redis` Python client. Here is an example of how to connect to a Redis server and perform some basic operations:

```python
#!/usr/bin/env python3
import redis

# Connect to Redis server
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Set a key-value pair
r.set('key', 'value')

# Get the value of a key
value = r.get('key')
print(value)
```

### Using Redis as a Simple Cache

Redis can also be used as a simple cache to store frequently accessed data. Here is an example of how to use Redis as a cache in Python:

```python
#!/usr/bin/env python3
import redis

# Connect to Redis server
cache = redis.Redis(host='127.0.0.1', port=6379, db=0)

def get_data(key):
    # Check if data is in cache
    if cache.exists(key):
        return cache.get(key)
    else:
        # Fetch data from a data source
        data = fetch_data_from_source(key)
        # Store data in cache
        cache.set(key, data)
        return data

def fetch_data_from_source(key):
    # Simulate data fetching from a data source
    return f"Data for {key}"

# Example usage
key = 'example_key'
data = get_data(key)
print(data)
```

## Conclusion

This project demonstrates the basics of using Redis for data storage and caching in Python. By following the provided instructions and examples, you will be able to effectively integrate Redis into your Python applications for improved performance and scalability.
