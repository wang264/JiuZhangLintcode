# 900. Closest Binary Search Tree Value
# 中文English
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Example
# Example1
#
# Input: root = {5,4,9,2,#,8,10} and target = 6.124780
# Output: 5
# Explanation：
# Binary tree {5,4,9,2,#,8,10},  denote the following structure:
#         5
#        / \
#      4    9
#     /    / \
#    2    8  10
# Example2
#
# Input: root = {3,2,4,1} and target = 4.142857
# Output: 4
# Explanation：
# Binary tree {3,2,4,1},  denote the following structure:
#      3
#     / \
#   2    4


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def build_binary_tree_from_list(arr):
    tree_nodes = [TreeNode(val) if val is not None else None for val in arr]

    root = tree_nodes[0]

    n = len(tree_nodes)
    for i in range(n):
        if tree_nodes[i] is None:
            continue

        left_index = i * 2 + 1
        right_index = i * 2 + 2

        if left_index < n:
            tree_nodes[i].left = tree_nodes[left_index]

        if right_index < n:
            tree_nodes[i].right = tree_nodes[right_index]

    return root


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here

        val, dis = self.closest_value_helper(root, target)
        return val

    def closest_value_helper(self, root, target):
        if root is None:
            return None, None
        root_distance = abs(root.val - target)

        left_val, left_distance = self.closest_value_helper(root.left, target)
        right_val, right_distance = self.closest_value_helper(root.right, target)

        # not child
        if left_val is None and right_val is None:
            return root.val, root_distance
        # only right child
        elif left_val is None and right_val is not None:
            if right_distance < root_distance:
                return right_val, right_distance
            else:
                return root.val, root_distance
        # only left child
        elif left_val is not None and right_val is None:
            if left_distance < root_distance:
                return left_val, left_distance
            else:
                return root.val, root_distance
        # have both left and right child
        else:
            if root_distance <= left_distance and root_distance <= right_distance:
                return root.val, root_distance
            elif left_distance <= root_distance and left_distance <= right_distance:
                return left_val, left_distance
            elif right_distance <= root_distance and right_distance <= left_distance:
                return right_val, right_distance


class Solution2:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        if root is None:
            return None

        lower = self.lower_bound(root, target)
        upper = self.upper_bound(root, target)
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val

        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val

    def lower_bound(self, root, target):
        # the largest number that are lower than target
        if root is None:
            return None

        if root.val > target:
            return self.lower_bound(root.left, target)
        else:
            lower = self.lower_bound(root.right, target)
            if lower is None:
                return root
            else:
                return lower

        pass

    def upper_bound(self, root, target):
        # the smallest number that are larger than target
        if root is None:
            return None

        if root.val < target:
            return self.upper_bound(root.right, target)
        else:
            upper = self.upper_bound(root.left, target)

            if upper is None:
                return root
            else:
                return upper


sol = Solution2()
root = build_binary_tree_from_list(arr=[5, 4, 9, 2, None, 8, 10])
sol.closestValue(root, 4.6)