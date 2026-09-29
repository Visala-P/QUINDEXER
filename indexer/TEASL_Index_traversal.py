def TEASL_traversal(search_version, levels):

    current_node = levels[-1][-1]

    closest_version = None
    fallback_version = None

    while True:

        if current_node.Version >= search_version:
            fallback_version = current_node.equal_node_pointer

        if (
            current_node.Version == search_version
            or (
                current_node.left_pointer is None
                and current_node.right_pointer is None
            )
        ):
            closest_version = current_node.equal_node_pointer
            break

        elif current_node.Version > search_version:

            if current_node.left_pointer is not None:
                current_node = current_node.left_pointer
                continue

            else:
                closest_version = current_node.equal_node_pointer
                break

        elif current_node.Version < search_version:

            if current_node.right_pointer is not None:
                current_node = current_node.right_pointer
                continue

            else:
                closest_version = current_node.equal_node_pointer
                break

    if closest_version.Version < search_version:
        closest_version = fallback_version

    return closest_version