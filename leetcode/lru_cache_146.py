# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of
# the key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key
# exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this
# operation, evict the least recently used key. Follow up: Could you do get and put in O(1) time complexity?

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._data_dict = OrderedDict()

    def get(self, key: int) -> int:
        if len(self._data_dict):
            if key in self._data_dict:
                value = self._data_dict.pop(key)
                self._data_dict[key] = value
                return value
            else:
                return -1
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        keyold = None
        if len(self._data_dict) == self._capacity and key not in self._data_dict:
            keyold = next(iter(self._data_dict))
        elif key in self._data_dict:
            keyold = key
        if keyold:
            self._data_dict.pop(keyold)
        self._data_dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
