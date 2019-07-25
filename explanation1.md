
# Least Recently Used Cache

Problem Statement: Design an LRU cache where all operations have O(1) constant complexity

Rationale of Solution:

The variables 'clock' and 'frames' are named after the lower-level CS terms for where LRU's are actually implemented by a machine's OS. Clock is a collection.deque (double ended queue). A deque was chosen because adding and removing to either end of the deque is O(1). New items are added to the end of the deque and old items are removed from the beginning.

Time/Space complexity:

All methods are O(1) because they use a dictionary and pop/append of a deque. For space complexity we have linear complexity up to the size of the cache.
