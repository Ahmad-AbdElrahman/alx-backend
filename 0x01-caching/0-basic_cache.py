#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system
    """
    def __init__(self):
        """
        initialize method
        """
        super().__init__()

    def put(self, key, item):
        """
        Put values method
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get values method
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)
