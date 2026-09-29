def append_only_skip_list_search(query_version, latest_version):
    """
    Searching algorithm for an append-only skip-list.
    Due to the nature of blockchain with immutability,
    appending is the only valid method type.
    """

    finish = False
    this_version = latest_version
    version_data = False

    while not finish:

        # If no pointers exist, it must be the first node version
        if not this_version.pre_nodes or not this_version.node_level:
            # Skip list is exhausted; data could not be located
            version_data = False
            finish = True

        # While the skip list contains items
        while this_version.pre_nodes and this_version.node_level:

            # Check skip-list nodes from highest version to lowest
            this_pre_node = this_version.pre_nodes[-1]

            if this_pre_node.Version == query_version:
                # Version found
                finish = True
                version_data = True
                break

            elif this_pre_node.Version < query_version:
                # Remove the left pointer from the lists
                this_version.pre_nodes.pop()
                this_version.node_level.pop()

            else:
                # Move to the previous node
                this_version = this_pre_node

                # Exit inner while loop
                break

    return version_data