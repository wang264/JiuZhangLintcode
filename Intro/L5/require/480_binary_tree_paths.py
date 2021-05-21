# Algorithm L4 require

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []

        curr_path = [str(root.val)]
        rslt = []

        self.dfs_helper(root, curr_path, rslt)

        return rslt

    def dfs_helper(self, node, curr_path, rslt):
        if node.left is None and node.right is None:
            # curr_path.append(str(node.val))
            rslt.append("->".join(curr_path))
            # curr_path.pop()
            return

        if node.left:
            curr_path.append(str(node.left.val))
            self.dfs_helper(node.left, curr_path, rslt)
            curr_path.pop()

        if node.right:
            curr_path.append(str(node.right.val))
            self.dfs_helper(node.right, curr_path, rslt)
            curr_path.pop()


