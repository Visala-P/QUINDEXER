from supporting_structures_TEASL import TEASL_Node


def TEASL_append(version, levels):
    """
    Append an EASL version to the TEASL index.

    TEASL is represented as a binary search tree.
    Each TEASL node points back to its corresponding EASL node.
    """

    new_node = TEASL_Node(version.Version)
    new_node.equal_node_pointer = version

    # First version becomes the root.
    if not levels:
        levels.append([new_node])
        return True

    # Collect the existing tree root.
    root = levels[-1][0]

    # Insert into the binary-search tree.
    current = root

    while True:

        if version.Version < current.Version:

            if current.left_pointer is None:
                current.left_pointer = new_node
                break

            current = current.left_pointer

        elif version.Version > current.Version:

            if current.right_pointer is None:
                current.right_pointer = new_node
                break

            current = current.right_pointer

        else:
            return True

    # Rebuild levels from the complete tree.
    tree_levels = []

    def collect(node, depth):
        if node is None:
            return

        while len(tree_levels) <= depth:
            tree_levels.append([])

        tree_levels[depth].append(node)

        collect(node.left_pointer, depth + 1)
        collect(node.right_pointer, depth + 1)

    collect(root, 0)

    # TEASL traversal expects:
    # levels[-1] = highest/root level
    levels.clear()

    for tree_level in reversed(tree_levels):
        levels.append(tree_level)

    return True