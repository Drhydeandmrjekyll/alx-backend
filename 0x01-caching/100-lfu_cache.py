#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq_counter = {}
        self.used_order = []

    def put(self, key, item):
        """Add item in cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Increment frequency counter for existing key
            self.freq_counter[key] += 1
        else:
            # Add new key to frequency counter
            self.freq_counter[key] = 1

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find key(s) with minimum frequency
            min_freq = min(self.freq_counter.values())
            min_freq_keys = [
                    k for k,
                    v in self.freq_counter.items() if v == min_freq]
            # If keys with minimum frequency,use LRU choose which to discard
            lru_key = min_freq_keys[0]
            for k in min_freq_keys:
                if k in self.used_order:
                    lru_key = k
                    break
            # Discard least frequency used item (LFU algorithm)
            del self.cache_data[lru_key]
            del self.freq_counter[lru_key]
            self.used_order.remove(lru_key)
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        if key in self.used_order:
            self.used_order.remove(key)
        self.used_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency counter for the accessed key
        self.freq_counter[key] += 1

        # Update usage order
        if key in self.used_order:
            self.used_order.remove(key)
        self.used_order.append(key)

        return self.cache_data[key]
