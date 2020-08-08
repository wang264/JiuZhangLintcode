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
