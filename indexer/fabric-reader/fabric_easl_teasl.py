import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from fabric_blocks_to_easl import build_easl
from TEASL_construction_algorithm import TEASL_append
from TEASL_Index_traversal import TEASL_traversal


print("================================")
print("Fabric → EASL → TEASL")
print("================================")

# Build EASL from real Fabric blocks
nodes = build_easl(6, 9)

# Build TEASL
levels = []

for node in nodes:
    result = TEASL_append(node, levels)

    print(
        f"EASL version {node.Version}: "
        f"TEASL processed = {result}"
    )

# Display TEASL
print("\nTEASL levels:")

for level_number, level in enumerate(levels):
    print(
        f"Level {level_number}: "
        f"{[node.Version for node in level]}"
    )

# Traversal
if levels:
    print("\nTraversal tests:")

    for search_version in [6, 7, 8, 9]:

        result = TEASL_traversal(
            search_version,
            levels
        )

        print(
            f"Search {search_version} "
            f"→ EASL version {result.Version}, "
            f"value = {result.Value}"
        )
