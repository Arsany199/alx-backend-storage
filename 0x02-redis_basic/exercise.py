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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """take a key string argument and an optional Callable argument
        named fnThis callable will be used to convert the data back
        to the desired format"""
        val = self._redis.get(key)
        return val if not fn else fn(val)

    def get_str(self, data: bytes) -> str:
        """bytes to string"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """bytes to int"""
        return int.from_bytes(data, sys.byteorder)
