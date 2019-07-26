
# Problem 2 File Recursion

Problem Statement: find all files under a directory (and all directories beneath it) that end with ".c"

Rationale of Solution:

Directories can be thought of as tree structures with files being leaves and directories being branches. Trees are usually searched recursively so the solution recursively searches branches for matching files. As a catch for extreme cases where OSError's may occur I've prevented common root paths from being the start of the search.

Time/Space complexity:

An OS often uses indexing/hashing of file names to make binary trees of files O(log(n)) for fast lookup. However this script doesn't take advantage of any of that. We load every leaf and branch into the script once for O(n) where n is the number of files in all the folders from the start point.

In terms of space complexity each path is read once so the complexity becomes O(n) where n represents each file and directory path from the initial path.
