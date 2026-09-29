from supporting_structures_EASL import Node
from TEASL_construction_algorithm import TEASL_append
from TEASL_Index_traversal import TEASL_traversal
from EASL_version_range_retrieval import append_only_skip_list_range_search

# --------------------------------------------------
# Create sample EASL nodes
# --------------------------------------------------
nodes = []

for version_number in range(1, 11):

    node = Node(
        version_number,
        f"block-{version_number}"
    )

    if version_number > 1:
        node.pre_nodes.append(nodes[-1])
        node.node_level.append(3)

    nodes.append(node)

# --------------------------------------------------
# Build TEASL
# --------------------------------------------------

levels = []

for node in nodes:

    result = TEASL_append(node, levels)

    print(
        f"EASL version {node.Version}: "
        f"TEASL processed = {result}"
    )


# --------------------------------------------------
# Display TEASL structure
# --------------------------------------------------

print("\nTEASL levels:")

for level_number, level in enumerate(levels):

    print(
        f"Level {level_number}: "
        f"{[node.Version for node in level]}"
    )


# --------------------------------------------------
# Test traversal
# --------------------------------------------------

if levels:

    print("\nTraversal tests:")

    for search_version in [3, 5, 7, 10]:

        result = TEASL_traversal(
            search_version,
            levels
        )

        print(
            f"Search {search_version} "
            f"→ EASL version {result.Version}, "
            f"value = {result.Value}"
        )
print("\nRange retrieval tests:")

ranges = [
    (3, 7),
    (1, 5),
    (6, 10),
]

for start, end in ranges:
    result = append_only_skip_list_range_search(
        start,
        end,
        nodes[-1]
    )

    print(f"Range {start} → {end}: {result}")