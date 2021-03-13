# 242. Convert Binary Tree to Linked Lists by Depth
# 中文English
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
# (e.g., if you have a tree with depth D, you'll have D linked lists).
#
# Example
# Example 1:
#
# Input: {1,2,3,4}
# Output: [1->null,2->3->null,4->null]
# Explanation:
#         1
#        / \
#       2   3
#      /
#     4
# Example 2:
#
# Input: {1,#,2,3}
# Output: [1->null,2->null,3->null]
# Explanation:
#     1
#      \
#       2
#      /
#     3


# Definition of TreeNode:
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
    forest = [TreeNode(x) if x is not None else None for x in sequence]

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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        lists = self.level_order_traversal(root=root)
        linked_list = self.build_linked_list(lists=lists)
        return linked_list

    def level_order_traversal(self, root):
        rslt = []
        if root is None:
            return rslt
        queue = deque([root])

        while queue:
            rslt_this_level = []
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                rslt_this_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            rslt.append(rslt_this_level)

        return rslt

    def build_linked_list(self, lists):
        linked_lists = []
        for list in lists:
            head = ListNode(-1)
            prev_node = head
            for element in list:
                curr_node = ListNode(element)
                prev_node.next = curr_node
                prev_node = curr_node
            linked_lists.append(head.next)

        return linked_lists


sol = Solution()
root = build_tree_breadth_first(sequence=[1, 2, 3, 4])
linked_list = sol.binaryTreeToLists(root=root)

from collections import deque


class Solution2:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if root is None:
            return []
        # Write your code here
        q = deque([root])

        rslt = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                list_node = ListNode(node.val)
                if i == 0:
                    rslt.append(list_node)
                    prev_node = list_node
                else:
                    prev_node.next = list_node
                    prev_node = list_node

        return rslt


sol = Solution()
root = build_tree_breadth_first(sequence=[1, 2, 3, 4])
linked_list = sol.binaryTreeToLists(root=root)
