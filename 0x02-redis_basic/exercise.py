#!/usr/bin/env python3
"""
Using Redis in Python
"""
import redis
import uuid
from typing import Callable, Union

def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self.redis_client.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """
    Cache class using Redis for python
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        id: str = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Callable = None):
        value = self._redis.get(key)
        if value is not None and fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str):
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str):
        return self.get(key, fn=lambda x: int(x))

