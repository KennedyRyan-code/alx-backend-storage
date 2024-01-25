#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable
named _redis (using redis.Redis()),
and flush the instance using flushdb.
"""


import uuid
import redis
from typing import Union, Callable
from functools import wraps


class Cache:
    """Create a cache class"""

    def __init__(self):
        """Store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """returns a Callable"""
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """Wrapper for decorated function"""
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def call_history(method: Callable) -> Callable:
        key_inputs = "{}:inputs".format(method.__qualname__)
        key_outputs = "{}:outputs".format(method.__qualname__)

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Use str(args) to normalize and store input parameters
            self._redis.rpush(key_inputs, str(args))

            # Execute the wrapped function to retrieve the output
            output = method(self, *args, **kwargs)

            # Store the output using rpush in the ":outputs" list
            self._redis.rpush(key_outputs, output)

            return output

        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, None]:
        """convert the data back to the desired format"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """automatically parametrize Cache.get with the right
        conversion function"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """automatically parametrize Cache.get with the right
        conversion function"""
        return self.get(key, fn=int)
