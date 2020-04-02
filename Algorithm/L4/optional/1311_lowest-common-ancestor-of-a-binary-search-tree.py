class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        #由于BST的性质，如果一个大一个小的话LCA一定是root，不然在其一侧子树上，递归寻找即可
        if root is None:
            return root

        if p is None or q is None:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val <= root.val <= p.val or p.val <= root.val <= q.val:
            return root