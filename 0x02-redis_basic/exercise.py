#!/usr/bin/env python3
"""model for redis"""
from functools import wraps
from typing import Union, Callable, Optional
import redis
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """initilize the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
