# 85. Insert Node in a Binary Search Tree
# 中文English
# Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.
#
# Example
# Example 1:
# 	Input:  tree = {}, node = 1
# 	Output:  1
# Explanation:
# 	Insert node 1 into the empty tree, so there is only one node on the tree.
#
# Example 2:
# 	Input: tree = {2,1,4,3}, node = 6
# 	Output: {2,1,4,3,6}
#
# Explanation:
# 	Like this:
#       2             2
# 	 / \           / \
# 	1   4   -->   1   4
# 	   /             / \
# 	  3             3   6
#
# Challenge
# Can you do it without recursion?
#
# Notice
# You can assume there is no duplicate values in this tree + node.

from helperfunc import build_tree_breadth_first, TreeNode


# method iteration
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        prev = None
        curr = root
        while curr is not None:
            prev = curr
            if node.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if node.val < prev.val:
            prev.left = node
        else:
            prev.right = node

        return root


# method recursion
class Solution2:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        root = self.traverse_and_try_insert(root, node)
        return root

    def traverse_and_try_insert(self, root, node):
        if root is None:
            return node
        if node.val < root.val:
            root.left = self.traverse_and_try_insert(root.left, node)
        else:
            root.right = self.traverse_and_try_insert(root.right, node)

        return root


sol = Solution2()
root = build_tree_breadth_first(sequence=[2, 1, 4, 3])
rslt = sol.insertNode(root,node=TreeNode(6))
