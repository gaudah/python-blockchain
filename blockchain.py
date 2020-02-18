import datetime as date
from block import Block
import random
from utils import constants,utils

class BlockChain():
    """
          Define blockchain
    """
    def __init__(self, difficulty):  # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]
        # difficulty of proof of work algorithm
        self.difficulty = difficulty

    """
        Create genesis block 
    """
    def get_genesis_block(self):
        print("\t ########################################## ADDING BLOCK TO BLOCKCHAIN    #################################     \n")
        print("Block #{} has been added to the blockchain!".format(0))
        return Block(0,
                     date.datetime.now(),
                    constants.GENESIS_BLOCK_DATA,
                    constants.GENESIS_BLOCK_HASH,0)

        print(" SUCC Block #{} has been added to the blockchain!".format(0))

    """
        Add new block 
    """
    def add_block(self, data):
        new_block = Block(len(self.blocks),
                                 date.datetime.now(),
                                 data,
                                 self.blocks[len(self.blocks) - 1].hash,1)

        update_hash_by_difficulty = new_block.mine_block(self.difficulty)
        self.blocks.append(new_block)
        print("\t ########################################## ADDING BLOCK TO BLOCKCHAIN    #################################     \n")
        print("Block #{} has been added to the blockchain!".format(len(self.blocks) - 1))

    """
        Add list of blocks 
    """
    def add_list_of_blocks(self,num_of_blocks_to_add):
        for block in range(0, num_of_blocks_to_add):
            self.add_block({
                'sender': utils.generate_string(constants.RANDOM_LENGTH)+ str(block),
                'recipient': utils.generate_string(constants.RANDOM_LENGTH) + str(block),
                'amount': random.randrange(constants.MIN_AMT, constants.MAX_AMT)})

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
                    print("\t ########################################## ERROR WHILE VALIDATING BLOCKCHAIN   #################################     \n")
                    print('Wrong block index at block {}.'.format(i))
            if self.blocks[i - 1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print("\t ########################################## ERROR WHILE VALIDATING BLOCKCHAIN   #################################     \n")
                    print('Wrong previous hash at block {}.'.format(i))
            if self.blocks[i].hash != self.blocks[i].hash_block():
                flag = False
                if verbose:
                    print("\t ########################################## ERROR WHILE VALIDATING BLOCKCHAIN   #################################     \n")
                    print('Wrong hash at block {}.'.format(i))
            if self.blocks[i - 1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print(" BOTH TIMESTAMP ARE :",self.blocks[i - 1].timestamp,self.blocks[i].timestamp)
                    print("\t ########################################## ERROR WHILE VALIDATING BLOCKCHAIN   #################################     \n")
                    print('Backdating at block {}.'.format(i))
        return flag
