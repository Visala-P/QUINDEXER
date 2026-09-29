class TEASL_Node:
    def __init__(self, version):
        self.Version = version
        self.left_pointer = None       # reference to left TEASL_Node
        self.equal_node_pointer = None # reference to Node
        self.right_pointer = None      # reference to right TEASL_Node