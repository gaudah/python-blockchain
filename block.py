import hashlib as hasher
from utils import constants

class Block:
    """
         Define block params
    """
    def __init__(self, index, timestamp, data, previous_hash, nonce):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.hash_block()

    """
          Calculate hash of the block
    """
    def hash_block(self):
        key = hasher.sha256()
        key.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.nonce).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()

    """
          Get block details
    """
    def get_block_data(self):
        return (self.index, self.timestamp, self.data,self.previous_hash,self.nonce)

    def mine_block(self,difficulty):
        while (self.hash[0:difficulty] != (constants.HASH_PREFIX * difficulty)):
            self.nonce = self.nonce + 1
            self.hash = self.hash_block()
        return 1