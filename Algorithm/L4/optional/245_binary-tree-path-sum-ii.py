# 246. Binary Tree Path Sum II
# 中文English
# Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which
# sum to a given value. The path does not need to start or end at the root or a leaf,
# but it must go in a straight line down.
#
# Example
# Example 1:
#
# Input:
# {1,2,3,4,#,2}
# 6
# Output:
# [[2, 4],[1, 3, 2]]
# Explanation:
# The binary tree is like this:
#     1
#    / \
#   2   3
#  /   /
# 4   2
# for target 6, it is obvious 2 + 4 = 6 and 1 + 3 + 2 = 6.
# Example 2:
#
# Input:
# {1,2,3,4}
# 10
# Output:
# []
# Explanation:
# The binary tree is like this:
#     1
#    / \
#   2   3
#  /
# 4
# for target 10, there is no way to reach it.


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    # the main function is using devide and conquer, which means the set of all solution is from the following
    # solution from left-subtree, solution from right-subtree, solution from root.
    # Solution from root is like the original problem, instead, we need to make decision on every node insted of
    # just on the leaf node
    def binaryTreePathSum2(self, root, target):
        # write your code here
        rslt = []
        if root is None:
            return rslt
        left_paths = self.binaryTreePathSum2(root.left, target)
        right_paths = self.binaryTreePathSum2(root.right, target)
        middle_paths = self.from_root_to_any(root, target)
        return left_paths + right_paths + middle_paths

    def from_root_to_any(self, root, target):
        rslt = []
        curr_path = []
        self.dfs_helper(root, target, curr_path, rslt)
        return rslt

    def dfs_helper(self, root, target, curr_path, rslt):
        if root is None:
            return root

        curr_path.append(root.val)
        if root.val == target:
            rslt.append(curr_path[:])
        self.dfs_helper(root.left, target - root.val, curr_path, rslt)
        self.dfs_helper(root.right, target - root.val, curr_path, rslt)
        curr_path.pop()


# use DFS two times, one DFS to traverse, one DFS to add target path(from it's root to any node.) to result.
class Solution2:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        # write your code here
        if root is None:
            return []
        rslt = []
        self.dfs_traverse(root, rslt, target)
        return rslt

    def dfs_traverse(self, node, rslt, target):
        if node is None:
            return
        self.dfs_select_path(node, rslt, [], target)

        self.dfs_traverse(root.left, rslt, target)
        self.dfs_traverse(root.right, rslt, target)

    def dfs_select_path(self, node, rslt, curr_path, target):
        if node is None:
            return
        curr_path.append(node.val)
        if node.val == target:
            rslt.append(curr_path[:])

        self.dfs_select_path(node.left, rslt, curr_path, target - node.val)
        self.dfs_select_path(node.right, rslt, curr_path, target - node.val)
        curr_path.pop()


from helperfunc import build_tree_breadth_first, TreeNode

sol = Solution2()
root = build_tree_breadth_first([1, 2, 3, 4, None, 2])
assert sol.binaryTreePathSum2(root, 6) == [[1, 3, 2], [2, 4]]
root = build_tree_breadth_first([1, -2, None, 1])
root.left.left.left = TreeNode(2)
assert sol.binaryTreePathSum2(root, 2) == [[1, -2, 1, 2], [2]]
