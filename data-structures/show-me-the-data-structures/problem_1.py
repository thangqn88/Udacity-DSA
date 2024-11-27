from collections import OrderedDict
from typing import Any, Optional
from collections import deque

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity if (capacity is not None and capacity > 0) else 0


    def get(self, key):
        try:
            if key not in self.cache:
                return -1
            else:
                value = self.cache.pop(key)
                self.cache[key] = value
                return value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            print("Can't perform operations, capacity cache is Zero")
            return
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache) >= self.capacity: 
            # If the cache is full, remove the oldest item
            self.cache.popitem(last=False)
        self.cache[key] = value
        


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache
    our_cache.set(5, 5)
    our_cache.set(6, 6) 
    our_cache.set(7, 7) 
    assert our_cache.get(4) == -1  # Returns -1, 4 was evicted

    # Test Case 2: Update the value of an existing key
    our_cache = LRU_Cache(2)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(1, 10)
    assert our_cache.get(1) == 10 
    assert our_cache.get(2) == 2
    # should return 2

    # Test Case 3: Edge case of a cache with 0 capacity
    our_cache = LRU_Cache(0)
    our_cache.set(1, 8) #should print some message like "Can't perform operations on 0 capacity cache"
    assert our_cache.get(1) == -1 # should return -1

    # Test Case 4: Edge case of a cache with null
    our_cache = LRU_Cache(None)
    our_cache.set(2, 11) #should print some message like "Can't perform operations on 0 capacity cache"
    assert our_cache.get(2) == -1 # should return -1
