from supporting_structures_EASL import Node
from supporting_structures_TEASL import TEASL_Node
from TEASL_Index_traversal import TEASL_traversal


# --------------------------------------------------
# Create EASL nodes
# --------------------------------------------------

nodes = {}

for version in range(1, 11):
    nodes[version] = Node(
        version,
        f"block-{version}"
    )


# --------------------------------------------------
# Manually create a simple TEASL structure
#
#             5
#           /   \
#          3     8
#         / \   / \
#        1   4 6  10
#
# This lets us verify traversal independently.
# --------------------------------------------------

n5 = TEASL_Node(5)
n3 = TEASL_Node(3)
n8 = TEASL_Node(8)
n1 = TEASL_Node(1)
n4 = TEASL_Node(4)
n6 = TEASL_Node(6)
n10 = TEASL_Node(10)


# Attach corresponding EASL nodes

n5.equal_node_pointer = nodes[5]
n3.equal_node_pointer = nodes[3]
n8.equal_node_pointer = nodes[8]
n1.equal_node_pointer = nodes[1]
n4.equal_node_pointer = nodes[4]
n6.equal_node_pointer = nodes[6]
n10.equal_node_pointer = nodes[10]


# Build traversal pointers

n5.left_pointer = n3
n5.right_pointer = n8

n3.left_pointer = n1
n3.right_pointer = n4

n8.left_pointer = n6
n8.right_pointer = n10


# --------------------------------------------------
# TEASL levels
# --------------------------------------------------

levels = [
    [n1, n3, n4, n5, n6, n8, n10]
]


# --------------------------------------------------
# IMPORTANT:
# traversal starts from levels[-1][-1]
#
# Therefore the highest/latest node must have
# the appropriate pointers.
#
# For this test, use n5 as the root by making it
# the last node of the highest level.
# --------------------------------------------------

levels = [
    [n1, n3, n4, n6, n8, n10],
    [n5]
]


# --------------------------------------------------
# Test traversal
# --------------------------------------------------

for search_version in [1, 3, 4, 5, 6, 8, 10]:

    result = TEASL_traversal(
        search_version,
        levels
    )

    print(
        f"Search {search_version} "
        f"→ EASL version {result.Version}, "
        f"value = {result.Value}"
    )