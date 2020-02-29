"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    # the main function is using devide and conquer, which means the set of all solution is from the following
    # solution from left-subtree, solution from right-subtree, solution from root.
    # Solution from root is like the original problem, instead, we need to make decision on every node insted of
    # just on the leaf node
    def binaryTreePathSum2(self, root, target):
        # write your code here
        rslt = []
        if root is None:
            return rslt
        left_paths = self.binaryTreePathSum2(root.left, target)
        right_paths = self.binaryTreePathSum2(root.right, target)
        middle_paths = self.from_root_to_any(root, target)
        return left_paths + right_paths + middle_paths

    def from_root_to_any(self, root, target):
        rslt = []
        curr_path= []
        self.dfs_helper(root, target, curr_path, rslt)
        return rslt

    def dfs_helper(self, root, target, curr_path, rslt):
        if root is None:
            return root

        curr_path.append(root.val)
        if root.val == target:
            rslt.append(curr_path[:])
        self.dfs_helper(root.left, target-root.val, curr_path, rslt)
        self.dfs_helper(root.right, target-root.val, curr_path, rslt)
        curr_path.pop()

# sol = Solution()
# root, _ = build_tree_from_list([1,-2,None,1,None,None,None,2])
# #root, _ = build_tree_from_list([1,2,3,4,None,2])
# sol.binaryTreePathSum2(root, 2)