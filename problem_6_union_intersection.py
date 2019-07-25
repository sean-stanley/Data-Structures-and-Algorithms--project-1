class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self._position = None

    def __str__(self):
        if not self.head:
            return "<empty linked list>"
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __iter__(self):
        self._position = self.head
        return self

    def __next__(self):
        if self._position is None:
            raise StopIteration

        value = self._position.value
        self._position = self._position.next
        return value


def union(llist_1, llist_2):
    """Union that removes duplicates and preserves order."""
    # Your Solution Here
    print('unioning')
    union_set = set(llist_1).union(set(llist_2))
    union_llist = LinkedList()
    val_set = set()
    # preserving order
    # iterating the set would be marginally faster
    for llist in (llist_1, llist_2):
        for val in llist:
            if val in union_set and val not in val_set:
                union_llist.append(val)
                val_set.add(val)

    return union_llist


def intersection(llist_1, llist_2):
    """Intersection that removes duplicates and preserves order."""
    print('intersecting...')
    intersect_set = set(llist_1).intersection(set(llist_2))
    intersect_list = LinkedList()
    val_set = set()
    # preserving order
    # iterating the set would be marginally faster
    for llist in (llist_1, llist_2):
        for val in llist:
            if val in intersect_set and val not in val_set:
                intersect_list.append(val)
                val_set.add(val)
    return intersect_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print (intersection(linked_list_1,linked_list_2))
# 4 -> 6 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# edge case for no intersection
print(union(linked_list_3, linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_3, linked_list_4))
# <empty linked list>
#

linked_list_5 = LinkedList()

for i in range(100, 400, 5):
    linked_list_5.append(i)

linked_list_6 = LinkedList()

for i in range(100, 400, 6):
    linked_list_6.append(i)

# edge case for huge list
print(union(linked_list_5, linked_list_6))
# 100 -> 105 -> 110 -> 115 -> 120 -> 125 -> 130 -> 135 -> 140 -> 145 -> 150 -> 155 -> 160 -> 165 -> 170 -> 175 -> 180 -> 185 -> 190 -> 195 -> 200 -> 205 -> 210 -> 215 -> 220 -> 225 -> 230 -> 235 -> 240 -> 245 -> 250 -> 255 -> 260 -> 265 -> 270 -> 275 -> 280 -> 285 -> 290 -> 295 -> 300 -> 305 -> 310 -> 315 -> 320 -> 325 -> 330 -> 335 -> 340 -> 345 -> 350 -> 355 -> 360 -> 365 -> 370 -> 375 -> 380 -> 385 -> 390 -> 395 -> 106 -> 112 -> 118 -> 124 -> 136 -> 142 -> 148 -> 154 -> 166 -> 172 -> 178 -> 184 -> 196 -> 202 -> 208 -> 214 -> 226 -> 232 -> 238 -> 244 -> 256 -> 262 -> 268 -> 274 -> 286 -> 292 -> 298 -> 304 -> 316 -> 322 -> 328 -> 334 -> 346 -> 352 -> 358 -> 364 -> 376 -> 382 -> 388 -> 394 ->

print(intersection(linked_list_5, linked_list_6))
# 100 -> 130 -> 160 -> 190 -> 220 -> 250 -> 280 -> 310 -> 340 -> 370 ->
#
