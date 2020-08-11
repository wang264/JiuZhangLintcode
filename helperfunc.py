class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def build_graph(input_str: str, values: list) -> list:
    nodes = [UndirectedGraphNode(val) for val in values]
    str_temp = input_str.split('{')[1].split('}')[0]
    strs_to_set_neighbors = str_temp.split('#')
    for the_str in strs_to_set_neighbors:
        node_idx_plus1, *neighbors_idx_plus1 = [int(x) for x in the_str.split(',')]
        for neighbor_idx_plus1 in neighbors_idx_plus1:
            nodes[node_idx_plus1 - 1].neighbors.append(nodes[neighbor_idx_plus1 - 1])

    return nodes

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return '(D:{}, L:{}, R:{})'.format(self.val, left, right)


def build_tree_breadth_first(sequence):
    # Create a list of trees
    forest = [TreeNode(x) if x is not None else None for x in sequence ]

    # Fix up the left- and right links
    count = len(forest)
    for index, tree in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = forest[right_index]

    for index, tree in enumerate(forest):
        print('[{}]: {}'.format(index, tree))
    return forest[0]  # root

