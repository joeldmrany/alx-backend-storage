#!/usr/bin/env python3
'''
starting with redis-server
'''

import redis
import uuid


class Cache:
    ''' very important class '''
    def __init__(self):
        ''' init you now it '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        ''' storing data '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
