#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Remove least recently used item (LRU)
            lru_key = self.used_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.used_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        # Update usage order
        self.used_order.remove(key)
        self.used_order.append(key)
        return self.cache_data[key]
