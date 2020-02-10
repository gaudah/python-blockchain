import sys
from blockchain import BlockChain

"""
    @param : number of blocks we want to add.
    @description : add list of blocks, validate the block chain and display it.
    @return : block chain info. 
"""
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
