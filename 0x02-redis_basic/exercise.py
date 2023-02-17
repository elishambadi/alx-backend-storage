#!/usr/bin/env python3
"""
Using Redis in Python
"""
import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    @wraps(method) # This allows it to decorate a method
    def wrapper(self, *args):
        inp_key = method.__qualname__+":inputs"
        self._redis.rpush(inp_key, str(args))

        out_key = method.__qualname__+":outputs"
        result = method(self, *args)
        self._redis.rpush(out_key, str(result))

        return result
    return wrapper

class Cache:
    """
    Cache class using Redis for python
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
