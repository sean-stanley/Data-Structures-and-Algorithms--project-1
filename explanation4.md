
# Active Directory

Problem Statement: Write a function that provides an efficient look up of whether the user is in a group.

Rationale of Solution:
  Since a group can contain users or more groups, we must search all nested groups users for the user we are searching for. A recursive search does exactly that. For every group we encounter check both the users for our match and the subgroups.

Time complexity:
  The time complexity of the function is O(n) as we do one main recursive search through the tree in the worst case visiting every group and user once.
