import sys
import os
import json
import base64

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from supporting_structures_EASL import Node


BLOCK_DIR = "indexer/fabric-reader/blocks"


def decode_value(value):
    try:
        return base64.b64decode(value).decode("utf-8")
    except Exception:
        return value


def read_block(block_number):

    path = os.path.join(
        BLOCK_DIR,
        f"block-{block_number}.json"
    )

    with open(path, "r") as f:
        block = json.load(f)

    entries = block.get("data", {}).get("data", [])

    if not entries:
        return None

    entry = entries[0]

    payload = entry.get("payload", {})
    channel_header = (
        payload
        .get("header", {})
        .get("channel_header", {})
    )

    actions = (
        payload
        .get("data", {})
        .get("actions", [])
    )

    if not actions:
        return None

    action = actions[0]

    chaincode_id = (
        action
        .get("payload", {})
        .get("action", {})
        .get("proposal_response_payload", {})
        .get("extension", {})
        .get("chaincode_id", {})
    )

    chaincode_input = (
        action
        .get("payload", {})
        .get("chaincode_proposal_payload", {})
        .get("input", {})
        .get("chaincode_spec", {})
        .get("input", {})
    )

    args = chaincode_input.get("args", [])
    args = [decode_value(arg) for arg in args]

    return {
        "block_number": int(block["header"]["number"]),
        "channel": channel_header.get("channel_id"),
        "transaction_id": channel_header.get("tx_id"),
        "chaincode": chaincode_id.get("name"),
        "chaincode_version": chaincode_id.get("version"),
        "function": args[0] if args else None,
        "arguments": args[1:]
    }


def build_easl(start_block, end_block):

    easl_nodes = []

    for block_number in range(start_block, end_block + 1):

        data = read_block(block_number)

        if data is None:
            print(
                f"Skipping block {block_number}: "
                "no application transaction"
            )
            continue

        node = Node(
            data["block_number"],
            data
        )

        # Link this version to the previous version.
        if easl_nodes:
            node.pre_nodes.append(easl_nodes[-1])
            node.node_level.append(0)

        easl_nodes.append(node)

        print(
            f"EASL version {node.Version}: "
            f"{node.Value['function']} "
            f"{node.Value['arguments']}"
        )

    return easl_nodes


if __name__ == "__main__":

    nodes = build_easl(6, 9)

    print("\n================================")
    print("EASL INDEX")
    print("================================")

    for node in nodes:
        previous = (
            node.pre_nodes[-1].Version
            if node.pre_nodes
            else None
        )

        print(
            f"Version {node.Version} "
            f"-> Previous: {previous}"
        )

    print("\nTotal EASL nodes:", len(nodes))
