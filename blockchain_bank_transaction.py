import sys
from blockchain import BlockChain
import json

# main for function call.
if __name__ == "__main__":
    """
        @param : number of blocks we want to add and difficulty i.e number of zeros we want as prefix for generating 
        new hash.
        @description : add list of blocks, validate the block chain and display it.
        @return : block chain info. 
    """
    try:
        print(" Input arguments are :",len(sys.argv))

        if (len(sys.argv) != 3):
            raise Exception('Invalid arguments passed ')

        num_of_blocks = int(sys.argv[1])
        obj = BlockChain(int(sys.argv[2]))

        """
            Modern computers can create a hash quickly thousands per second. Also we can simply change any hash and
            quickly recalculate all previous hashes of block and end up with a valid chain.
            Proof of work -> With this mechanism you have to proof the input a lot of computing power to make a block. 
            This process is also called as mining.
            Here we need mining because some blocks are getting created immediately at same timestamp.
        """

        is_chain_valid = obj.add_list_of_blocks(num_of_blocks,obj)
        print("\t ########################################## CHECK CHAIN IS VALID :{}   #################################     \n".format(is_chain_valid))
        if(is_chain_valid == False):
            raise Exception("Invalid chain while adding new block..")
        block_chain_length = obj.get_chain_size()
        print("\t ########################################## FINDING BLOCKCHAIN LENGTH :   #################################     \n")
        print("Block chain length is : {}".format(block_chain_length))

        '''is_valid_chain = obj.check_chain_is_valid()
        print("\t ########################################## CHECK BLOCK IS VALID 1 :  #################################     \n")
        print("Block chain is_valid_chain ?  : {}".format(is_valid_chain))'''

        '''print("\t ########################################## UPDATE DATA OF FIRST BLOCK :  #################################     \n")

        obj.get_block_chain()[1].data = "updated"
        obj.get_block_chain()[1].hash = obj.get_block_chain()[1].hash_block()
        is_valid_chain = obj.check_chain_is_valid()
        print("\t ########################################## CHECK BLOCK IS VALID 2 :   #################################     \n")
        print("Block chain is_valid_chain ?  : {}".format(is_valid_chain))'''

        print("\t ########################################## BLOCK DETAILS ARE :   #################################     \n")
        new_dict = {}
        for index,obj in enumerate(obj.get_block_chain()):
            sub_dict = {}
            print("Block #{} details are !".format(obj.index))
            sub_dict.update(index=obj.index)
            sub_dict.update(timestamp=str(obj.timestamp))
            sub_dict.update(data=obj.data)
            sub_dict.update(previous_hash=obj.previous_hash)
            sub_dict.update(nonce=obj.nonce)
            sub_dict.update(hash=obj.hash)
            print("{}".format(json.dumps(sub_dict, sort_keys=True, indent=4)))
            key = "Block {}".format(index)
            new_dict[key] = sub_dict

        print("\t ########################################## FINAL BLOCKCHAIN : #################################     \n")
        print("{}".format(json.dumps(new_dict, sort_keys=True, indent=4)))

    except Exception as e:
        print("\t ########################################## ERROR :   #################################     \n")
        print(" Error is : {} ".format(e))
        print(" Invalid arguments passed: Input should be the number of blocks you want to add ")
        sys.exit(1)
