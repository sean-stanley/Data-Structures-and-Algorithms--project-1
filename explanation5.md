
# Blockchain

Problem Statement: Design a basic Blockchain Class

Rationale of Solution:

The linking of the block chain is done with a previous pointer referencing the previous block instance. Since blockchains are meant to be difficult to mutate, no pop, delete, insert, or appendLeft methods were needed for this linkedList. It would also have been possible to have the next block hash all the previous hashes to always get larger and more complicated hashes. This would create the "proof-of-work" aspect that many block-chains have. However I wasn't sure this was a requirement for this exercise so I simplified the strategy.

Time/Space complexity:
  Searching the block chain approaches O(n) for older blocks and is O(1) for most recent blocks. appending is O(1). The blockchain gets larger in memory for each block appended to it like O(n) where n is the size of each block.
