# 480. Binary Tree Paths
# 中文English
# Given a binary tree, return all root-to-leaf paths.
#
# Example
# Example 1:
#
# Input：{1,2,3,#,5}
# Output：["1->2->5","1->3"]
# Explanation：
#    1
#  /   \
# 2     3
#  \
#   5
# Example 2:
#
# Input：{1,2}
# Output：["1->2"]
# Explanation：
#    1
#  /
# 2


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        rslt = []
        this_path = []
        self.helper(root, this_path, rslt)
        return rslt

    def helper(self, node, this_path, rslt):
        # if this node is leave node
        this_path.append(str(node.val))
        if node.left is None and node.right is None:
            temp_str = '->'.join(this_path)
            rslt.append(temp_str)
        else:
            if node.left:
                self.helper(node.left, this_path, rslt)
                this_path.pop()
            if node.right:
                self.helper(node.right, this_path, rslt)
                this_path.pop()


# divide and conquer
class Solution2:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        paths = self.tree_path_helper(root)
        return ['->'.join(path) for path in paths]

    def tree_path_helper(self, root):
        # write your code here
        if root is None:
            return []
        left_paths = self.tree_path_helper(root.left)
        right_paths = self.tree_path_helper(root.right)

        paths = left_paths + right_paths
        if len(paths) == 0:
            return [[str(root.val)]]
        else:
            for path in paths:
                path.insert(0, str(root.val))

        return paths


# DFS
class Solution3:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []

        paths = []
        this_path = [str(root.val)]
        self.dfs(root, this_path, paths)
        return paths

    def dfs(self, node, this_path, paths):
        if node.left is None and node.right is None:
            paths.append('->'.join(this_path))

        if node.left:
            this_path.append(str(node.left.val))
            self.dfs(node.left, this_path, paths)
            this_path.pop()

        if node.right:
            this_path.append(str(node.right.val))
            self.dfs(node.right, this_path, paths)
            this_path.pop()


from helperfunc import build_tree_breadth_first

sol = Solution3()
root = build_tree_breadth_first(sequence=[1, 2, 3, None, 5])
sol.binaryTreePaths(root=root)
