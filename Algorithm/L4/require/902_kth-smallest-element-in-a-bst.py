# 902. Kth Smallest Element in a BST
# 中文English
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Example
# Example 1:
#
# Input：{1,#,2},2
# Output：2
# Explanation：
# 	1
# 	 \
# 	  2
# The second smallest element is 2.
# Example 2:
#
# Input：{2,1,3},1
# Output：1
# Explanation：
#   2
#  / \
# 1   3
# The first smallest element is 1.
# Challenge
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
# How would you optimize the kthSmallest routine?
#
# Notice
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):

        if root is None:
            return root

        count = 0
        stack = []
        rslt = []
        node = root

        while True:
            if node:
                stack.append(node)
                node = node.left

            elif stack:
                node = stack.pop()
                rslt.append(node.val)
                count += 1
                if count == k:
                    return node.val
                #if node.right:
                node = node.right
            else:
                break


class Solution2:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            # if not stack:
            #     return None

        return stack[-1].val

# sol = Solution()
# root = build_tree_from_list([1,None,2])
#
# sol.kthSmallest(root, 2)


