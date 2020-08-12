# Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.
#
# Example
# Example1
#
# Input: {1,2,3,4},6
# Output: [[2, 4],[2, 1, 3],[3, 1, 2],[4, 2]]
# Explanation:
# The tree is look like this:
#     1
#    / \
#   2   3
#  /
# 4
# Example2
#
# Input: {1,2,3,4},3
# Output: [[1,2],[2,1],[3]]
# Explanation:
# The tree is look like this:
#     1
#    / \
#   2   3
#  /
# 4


"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum3(self, root, target):
        # write your code here
        if not root:
            return []

        res = []
        self.dfs_traverse(root, res, target)

        return res

    def dfs_traverse(self, root, res, target):
        if not root:
            return

        visited = set()
        self.dfs_find_answer(root, res, [], visited, target)

        self.dfs_traverse(root.left, res, target)
        self.dfs_traverse(root.right, res, target)

    def dfs_find_answer(self, root, res, path, visited, target):
        if not root:
            return
        if root in visited:
            return

        visited.add(root)
        path.append(root.val)

        if root.val == target:
            res.append(path[:])

        self.dfs_find_answer(root.left, res, path, visited, target - root.val)
        self.dfs_find_answer(root.right, res, path, visited, target - root.val)
        self.dfs_find_answer(root.parent, res, path, visited, target - root.val)

        path.pop()
        visited.remove(root)


