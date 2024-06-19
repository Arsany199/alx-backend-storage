#!/usr/bin/env python3
"""web cache and tracker"""
import requests
import redis
from functools import wraps

s = redis.Redis()


def count_url_access(method):
    """counting how many times URL is accessed"""
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        s.incr(count_key)
        s.set(cached_key, html)
        s.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text
