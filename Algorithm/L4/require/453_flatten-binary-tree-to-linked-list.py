# 453. Flatten Binary Tree to Linked List
# 中文English
# Flatten a binary tree to a fake "linked list" in pre-order traversal.
#
# Here we use the right pointer in TreeNode as the next pointer in ListNode.
#
# Example
# Example 1:
#
# Input:{1,2,5,3,4,#,6}
# Output：{1,#,2,#,3,#,4,#,5,#,6}
# Explanation：
#      1
#     / \
#    2   5
#   / \   \
#  3   4   6
#
# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6
# Example 2:
#
# Input:{1}
# Output:{1}
# Explanation：
#          1
#          1
# Challenge
# Do it in-place without any extra memory.
#
# Notice
# Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        if root is None:
            return root
        dummy_node = TreeNode(-1)  # dummy node
        prev_node = dummy_node
        stack = [root]
        while stack:
            curr_node = stack.pop()
            prev_node.left = None
            prev_node.right = curr_node
            prev_node = curr_node

            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)

        return dummy_node.right


from helperfunc import TreeNode, build_tree_breadth_first

sol = Solution()
root = build_tree_breadth_first(sequence=[1, 2, 5, 3, 4, None, 6])
linked_list = sol.flatten(root)