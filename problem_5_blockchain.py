import hashlib
from datetime import datetime


def calc_hash(data):
    """Convert data represented as a string to a hash."""
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:
    """
    Block class for Blockchain.

    Parameters:
        data: string
        previous_hash: hexdigest hash string of linked Block
        timestamp: date, defaults to time of creation
    """

    def __init__(self, data, previous_hash, timestamp=datetime.utcnow()):
        """Block for Blockchain."""
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous = None
        self.hash = calc_hash(self.data)

    def __str__(self):
        s = f'''
            timestamp: {self.timestamp}
            data: {self.data}
            hash: {self.hash}
            previous_hash: {self.previous_hash}
        '''
        return s


class Blockchain:
    """Blockchain class."""

    def __init__(self):
        """Init the tail of the blockchain. Effectively the head."""
        self.tail = None

    def append(self, value):
        """Add a new block to the chain."""
        if self.tail is None:
            self.tail = Block(value, 0)
            return

        new_block = Block(value, self.tail.hash)
        new_block.previous = self.tail
        self.tail = new_block

    def search(self, value):
        """Search for a block with the requested value and return the block."""
        if self.tail is None:
            return None

        block = self.tail
        while block:
            if block.data == value:
                return block
            block = block.previous

        raise ValueError("Value not found in the blockchain.")

    def remove(self, value):
        """No-op. Deleting a block from a blockchain is not supported."""

    def top(self):
        """Return the most recent block"""
        return self.tail

    def size(self):
        """Return the length of the blockchain."""
        size = 0
        node = self.tail
        while node:
            size += 1
            node = node.previous

        return size

# tests
bc = Blockchain()

bc.append('foo')
bc.append('bar')
bc.append('flux')

print(bc.size())
# returns 3

print(bc.top().previous)
# returns most recent block

print(bc.search('foo'))
# returns the first block with previous_hash: 0

bc.append('foo')
print(bc.size())
# returns 4

print(bc.top())
# returns top block with same hash as first block.
