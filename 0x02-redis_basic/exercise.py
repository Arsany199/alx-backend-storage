#!/usr/bin/env python3
"""model for redis"""
from functools import wraps
from typing import Union, Callable, Optional
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """takes a single method Callable argument and returns a Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """def wrapper"""
        key_name = method.__qualname__
        self._redis.incr(key_name, 0) + 1
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function
    Everytime the original function will be called"""
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """def wrapp"""
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res
    return wrapper


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
