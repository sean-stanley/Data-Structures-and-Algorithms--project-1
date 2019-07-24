
# Union and Intersection of linkedList

Problem Statement: Design a basic Blockchain Class

Rationale of Solution:

The LinkedList class provided was expanded to include an __iter__ and __next__ methods to allow easy transformation of a linkedList into a Set or used with a for loop. However the question didn't specify whether the union should remove duplicates or preserve order. However, the time complexity would be marginally smaller in the average case if order wasn't preserved.

Time complexity:
  Union and intersection's time complexity is (O(n+m)) because each value in each linked_list is touched once. If order was discarded the time complexity would be (O(n)) where n was the number of elements in the returned list as the returned linked list must be created by iteration.
