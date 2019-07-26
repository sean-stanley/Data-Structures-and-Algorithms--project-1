from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.clock = deque()
        self.frames = {}
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # raise exception if capacity is 0
        if self.capacity <= 0:
            return Exception('Cannot perform "get" on 0 capacity cache.')
        value = self.frames.get(key, -1)
        self.clock.append(key)
        self.check_capacity()

        return value

    def set(self, key, value):
        """
        Set the value at key in the cache.

        key: any keyable value
        value: any
        """
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # set the key
        self.frames[key] = value

        # check capacity
        self.clock.append(key)
        self.check_capacity()

    def check_capacity(self):
        if len(self.clock) > self.capacity:
            key_to_delete = self.clock.popleft()
            self.frames.pop(key_to_delete, -1)

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# edge case 1 -- None key
our_cache.set(None, 3)
print(our_cache.get(None))  # returns 3

# edge case 0 capacity cache

empty_cache = LRU_Cache(0)

empty_cache.set(1,1)

print(empty_cache.get(1))
# print: Cannot perform "get" on 0 capacity cache.
