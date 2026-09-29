class Node:
    def __init__(self, version, value):
        self.Version = version              # version of identifier
        self.Value = value                  # state value for version
        self.pre_nodes = []                 # pointers/references to earlier nodes
        self.node_level = []                # level of each associated pre_node