class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if root is None:
            return []

        rslt = []
        self.dfs_helper(node=root, curr_path=[], curr_sum=0, target=target, rslt=rslt)
        return rslt

    def dfs_helper(self, node, curr_path, curr_sum, target, rslt):
        if node is None:
            return

        if node.left is None and node.right is None and curr_sum + node.val == target:  # we get the leaf node
            rslt.append(curr_path+[node.val])
        else:
            curr_path.append(node.val)
            self.dfs_helper(node.left, curr_path, curr_sum+node.val, target, rslt)
            self.dfs_helper(node.right, curr_path, curr_sum+node.val, target, rslt)
            curr_path.pop()