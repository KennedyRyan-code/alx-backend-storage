#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable
named _redis (using redis.Redis()),
and flush the instance using flushdb.
"""


import uuid
import redis
from typing import Union


class Cache:
    """Create a cache class"""

    def __init__(self):
        """Store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
