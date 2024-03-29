
# Huffman Coding

Problem Statement: create huffman encoding, decoding, and sizing schemas

Rationale of Solution:
  Tuples were chosen to store the tree in as they could be searched and nested recursively. Once the tree was built and constructed the encoding for a letter could be found by recording a 0 for traversing the tree left and a 1 for traversing the tree right until the leaf was arrived at. It did require an intermediate step to create the tree involving the branches in order to get the hierarchy correct. I'd be interested if there are more efficient ways of tree construction from the frequency of the letters. I wanted to avoid a massive tree class though like we used in the sample problems to keep the file smaller and simpler.

Time/Space complexity:
  Encoding and decoding iterate through each character like O(n) but then once they begin searching the tree the average case looks more like O(n log(n)) for both functions because searching the binary tree means we don't need to search every value for the match.

  In terms of space complexity for encoding, the data is stored temporarily in several intermediary forms, as a tree containing join nodes, a trimmed_tree and dictionary of codes. This can be represented as O(n + m + l + j) where n is the size of the initial input string, m is the untrimmed tree, l the trimmed tree and j the dictionary of codes.

  Decoding has linear space complexity as a variable is created for each bit in the data to be decoded. This can be represented as O(n) where n is each bit in the stream to decode.
