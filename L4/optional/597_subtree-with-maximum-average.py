import sys


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        # write your code here
        max_avg, max_tree, _, _ = self.helper(root)
        return max_tree

    def helper(self, node):
        """
        :param node:
        :return: tuple of 4
        the avgerage of the subtree that have maximum average,
        the root of the subtree that have maximum average,
        subtree size, number of nodes
        subtree sum of node value
        """
        if node is None:
            return -sys.maxsize, None, 0, 0

        l_max_avg, l_max_tree, l_size, l_sum = self.helper(node.left)
        r_max_avg, r_max_tree, r_size, r_sum = self.helper(node.right)

        cur_size, cur_sum = l_size + r_size + 1, l_sum + r_sum + node.val
        cur_avg = cur_sum / cur_size
        if l_max_avg == max(l_max_avg, r_max_avg, cur_avg):
            return l_max_avg, l_max_tree, cur_size, cur_sum
        elif r_max_avg == max(l_max_avg, r_max_avg, cur_avg):
            return r_max_avg, r_max_tree, cur_size, cur_sum
        else:
            return cur_avg, node, cur_size, cur_sum