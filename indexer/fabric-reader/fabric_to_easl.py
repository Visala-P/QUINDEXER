import sys
import os

# Allow imports from the indexer directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from supporting_structures_EASL import Node
from fabric_reader import read_latest_block


def create_easl_node():

    block_data = read_latest_block()

    if block_data is None:
        print("No Fabric block data found.")
        return None

    block_number = block_data["block_number"]

    value = {
        "block_number": block_number,
        "channel": block_data["channel"],
        "transaction_id": block_data["transaction_id"],
        "chaincode": block_data["chaincode"],
        "function": block_data["function"],
        "arguments": block_data["arguments"]
    }

    node = Node(block_number, value)

    print("\n================================")
    print("Fabric → EASL")
    print("================================")
    print("EASL Version:", node.Version)
    print("EASL Value:")
    print(node.Value)

    return node


if __name__ == "__main__":
    create_easl_node()
