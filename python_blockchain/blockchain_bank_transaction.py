import sys
from blockchain import BlockChain
#import python_blockchain
#from .blockchain import BlockChain
import json

# main for function call.
if __name__ == "__main__":
    """
        @param : number of blocks we want to add.
        @description : add list of blocks, validate the block chain and display it.
        @return : block chain info. 
    """
    try:
        #print(" Input arguments are :",len(sys.argv))
        #if(len(sys.argv) > 3 or len(sys.argv) < 2):
        #    raise Exception('Invalid arguments passed ')

        obj = BlockChain()
        num_of_blocks = int(4)
        obj.add_list_of_blocks(num_of_blocks)
        block_chain_length = obj.get_chain_size()
        print("\t ########################################## FINDING BLOCKCHAIN LENGTH    #################################     \n")
        print("Block chain length is : {}".format(block_chain_length))

        """
           Here we need mining because some blocks are getting created immediately at same timestamp.
        """
        is_valid_chain = obj.check_chain_is_valid()
        print("\t ########################################## CHECK BLOCK IS VALID    #################################     \n")
        print("Block chain is_valid_chain ?  : {}".format(is_valid_chain))

        print("\t ########################################## BLOCK DETAILS ARE    #################################     \n")
        new_dict = {}
        for index,obj in enumerate(obj.get_block_chain()):
            sub_dict = {}
            print("Block #{} details are !".format(obj.index))
            sub_dict.update(index=obj.index)
            sub_dict.update(timestamp=str(obj.timestamp))
            sub_dict.update(data=obj.data)
            sub_dict.update(previous_hash=obj.previous_hash)
            sub_dict.update(hash=obj.hash)
            print("{}".format(json.dumps(sub_dict, sort_keys=True, indent=4)))
            key = "Block {}".format(index)
            new_dict[key] = sub_dict

        print("\t ########################################## FINAL BLOCKCHAIN  #################################     \n")
        print("{}".format(json.dumps(new_dict, sort_keys=True, indent=4)))

    except Exception as e:
        print("\t ########################################## ERROR    #################################     \n")
        print(" Error is : {} ".format(e))
        print(" Invalid arguments passed: Input should be the number of blocks you want to add ")
        sys.exit(1)
