import json
import os
import base64


BLOCK_FILE = "indexer/fabric-reader/blocks/latest.json"


def decode_value(value):
    try:
        return base64.b64decode(value).decode("utf-8")
    except Exception:
        return value


def read_latest_block():

    if not os.path.exists(BLOCK_FILE):
        print("Block file not found:", BLOCK_FILE)
        return

    with open(BLOCK_FILE, "r") as f:
        block = json.load(f)

    block_number = int(block["header"]["number"])

    print("================================")
    print("Fabric Block Reader")
    print("================================")
    print("Block number:", block_number)

    data_entries = block.get("data", {}).get("data", [])

    print("Entries:", len(data_entries))

    if not data_entries:
        return None

    entry = data_entries[0]

    payload = entry.get("payload", {})
    header = payload.get("header", {})
    channel_header = header.get("channel_header", {})

    channel_id = channel_header.get("channel_id")
    tx_id = channel_header.get("tx_id")

    actions = payload.get("data", {}).get("actions", [])

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
        .get("action", {})
        .get("chaincode_proposal_payload", {})
        .get("input", {})
        .get("chaincode_spec", {})
        .get("input", {})
    )

    args = chaincode_input.get("args", [])
    decoded_args = [decode_value(arg) for arg in args]

    result = {
        "block_number": block_number,
        "channel": channel_id,
        "transaction_id": tx_id,
        "chaincode": chaincode_id.get("name"),
        "chaincode_version": chaincode_id.get("version"),
        "function": decoded_args[0] if decoded_args else None,
        "arguments": decoded_args[1:]
    }

    for index, entry in enumerate(data_entries):

        payload = entry.get("payload", {})
        header = payload.get("header", {})
        channel_header = header.get("channel_header", {})

        channel_id = channel_header.get("channel_id")
        tx_type = channel_header.get("type")
        tx_id = channel_header.get("tx_id")

        print("\nTransaction", index + 1)
        print("----------------")
        print("Channel:", channel_id)
        print("Transaction ID:", tx_id)
        print("Transaction type:", tx_type)

        transaction = payload.get("data", {})
        actions = transaction.get("actions", [])

        print("Actions:", len(actions))

        for action_index, action in enumerate(actions):

            chaincode_input = (
                action
                .get("payload", {})
                .get("action", {})
                .get("chaincode_proposal_payload", {})
                .get("input", {})
                .get("chaincode_spec", {})
                .get("input", {})
            )

            args = chaincode_input.get("args", [])

            decoded_args = [decode_value(arg) for arg in args]

            chaincode_id = (
                action
                .get("payload", {})
                .get("action", {})
                .get("proposal_response_payload", {})
                .get("extension", {})
                .get("chaincode_id", {})
            )

            print("\n Action", action_index + 1)
            print(" Chaincode:", chaincode_id.get("name"))
            print(" Chaincode version:", chaincode_id.get("version"))
            print(" Function:", decoded_args[0] if decoded_args else None)
            print(" Arguments:", decoded_args[1:])

    return result


if __name__ == "__main__":
    read_latest_block()
