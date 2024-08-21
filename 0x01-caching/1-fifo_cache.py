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
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Get values method
        """
        return self.cache_data.get(key, None)
