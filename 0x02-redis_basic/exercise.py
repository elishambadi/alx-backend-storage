#!/usr/bin/env python3
"""
Using Redis in Python
"""
import redis
import uuid


class Cache:
    """
    Cache class using Redis for python
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
