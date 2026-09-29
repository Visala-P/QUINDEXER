def append_only_skip_list_range_search(query_version_start, query_version_end, latest_version):
    """
    Searching algorithm for an append-only skip-list version range query.

    Due to the nature of blockchain with immutability,
    appending is the only valid method type.
    """

    finish = False
    this_version = latest_version
    version_data = []

    while not finish:

        if query_version_end == latest_version.Version:

            this_version = latest_version

            while this_version.Version >= query_version_start:

                version_data.insert(0, this_version.Value)

                if this_version.Version == query_version_start:
                    break

                if not this_version.pre_nodes:
                    break

                this_version = this_version.pre_nodes[0]

            break

        elif not this_version.pre_nodes or not this_version.node_level:
            break

        # While the skip-list contains items
        while this_version.pre_nodes and this_version.node_level:

            # Check skip-list nodes from highest version to lowest
            this_pre_node = this_version.pre_nodes[-1]

            if this_pre_node.Version == query_version_end:

                # Start from the end version
                this_version = this_pre_node

                # Walk backward through the bottom EASL level
                while this_version.Version >= query_version_start:

                    version_data.insert(0, this_version.Value)

                    if this_version.Version == query_version_start:
                        break

                    if not this_version.pre_nodes:
                        break

                    # Move to the previous version
                    this_version = this_version.pre_nodes[0]

                # Version range found
                finish = True
                break

            elif this_pre_node.Version < query_version_end:

                # Remove the left pointer from the list
                this_version.pre_nodes.pop()
                this_version.node_level.pop()

            else:

                # Update current version to pre-node
                this_version = this_pre_node

                # Exit inner while loop
                break

    return version_data