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
        """
        initialize method
        """
        super().__init__()

    def put(self, key, item):
        """
        Put values method
        """
        if key is None or item is None:
            return

        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f"DISCARD {first_item}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Get values method
        """
        return self.cache_data.get(key, None)
