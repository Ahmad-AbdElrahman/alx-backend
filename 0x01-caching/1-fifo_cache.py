#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None

        return self.cache_data.get(key, None)
