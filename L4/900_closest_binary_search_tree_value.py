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

        left_index = i*2+1
        right_index = i*2+2

        if left_index<n:
            tree_nodes[i].left = tree_nodes[left_index]

        if right_index<n:
            tree_nodes[i].right = tree_nodes[right_index]

    return root


class Solution:
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


