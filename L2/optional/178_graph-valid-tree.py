from collections import deque, defaultdict


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        neighbors = defaultdict(list)

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    q.append(neighbor)

        return len(visited) == n
        