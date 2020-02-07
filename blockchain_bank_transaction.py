import hashlib as hasher
import datetime as date
import sys

class Block:
    """
         Define block params
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    """
          Calculate hash of the block
    """
    def hash_block(self):
        key = hasher.sha256()
        key.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()

    """
          Get block details
    """
    def get_block_data(self):
        return (self.index, self.timestamp, self.data,self.previous_hash)


class BlockChain():
    """
          Define blockchain
    """
    def __init__(self):  # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]

    """
        Create genesis block 
    """
    def get_genesis_block(self):
        print("Block #{} has been added to the blockchain!".format(0))
        return Block(0,
                     date.datetime.now(),
                    'Genesis',
                    'arbitrary')

    """
        Add new block 
    """
    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks),
                                        date.datetime.utcnow(),
                                        data,
                                        self.blocks[len(self.blocks) - 1].hash))

        print("Block #{} has been added to the blockchain!".format(len(self.blocks) - 1))

    """
        Add list of blocks 
    """
    def add_list_of_blocks(self,num_of_blocks_to_add):
        for block in range(0, num_of_blocks_to_add):
            obj.add_block({
            'sender': "Aishwarya"+str(block),
            'recipient': "Sapana"+str(block),
            'amount': 5000 })

    """
        Get block chain size  
    """
    def get_chain_size(self):  # exclude genesis block
        return len(self.blocks) - 1

    """
        Get blockchain details  
    """
    def get_block_chain(self):
        return self.blocks

    """
        Get latest block added  
    """
    def get_latest_block(self):
        return self.blocks[-1]

    """
        Check blockchain is valid or not  
    """
    def check_chain_is_valid(self):
        flag = True
        verbose = True
        for i in range(1, len(self.blocks)):
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print('Wrong block index at block {i}.')
            if self.blocks[i - 1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print('Wrong previous hash at block {i}.')
            if self.blocks[i].hash != self.blocks[i].hash_block():
                flag = False
                if verbose:
                    print('Wrong hash at block {i}.')
            if self.blocks[i - 1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print('Backdating at block {i}.')
        return flag


# main for function call.
if __name__ == "__main__":
    try:
        print(" Input arguments are :",len(sys.argv))
        if(len(sys.argv) > 3 or len(sys.argv) < 2):
            raise Exception('Invalid arguments passed ')

        obj = BlockChain()
        num_of_blocks = int(sys.argv[1])
        obj.add_list_of_blocks(num_of_blocks)
        block_chain_length = obj.get_chain_size()
        print(" Block chain length is :",block_chain_length)

        """
           Here we need mining because some blocks are getting created immediately at same timestamp.
        """
        is_valid_chain = obj.check_chain_is_valid()
        print(" Block chain is_valid_chain ? ",is_valid_chain)

        for obj in obj.get_block_chain():
            print("Block #{} details are !".format(obj.index))
            print(obj.index, obj.timestamp, obj.data, obj.previous_hash, obj.hash)
    except Exception as e:
        print(" Error is :",e)
        print(" Invalid arguments passed: Input should be the number of blocks you want to add ")
        sys.exit(1)
