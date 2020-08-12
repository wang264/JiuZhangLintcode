# 1311. Lowest Common Ancestor of a Binary Search Tree
# 中文English
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}
#
# 图片
#
# Example
# Example 1:
#
# Input:
# {6,2,8,0,4,7,9,#,#,3,5}
# 2
# 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
# Input:
# {6,2,8,0,4,7,9,#,#,3,5}
# 2
# 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Notice
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.

# 解题思路
# 这道题与88. 最近公共祖先相似，都是求树内两个节点的最近公共祖先（LCA），我们本题也继续采用深度优先搜索（DFS）的方法。
# 不同的是，这道题明确指出这是二叉搜索树（BST），我们复习一下BST的性质：
# 对任意节点N，左子树上的所有节点的值都小于等于节点N的值
# 对任意节点N，右子树上的所有节点的值都大于等于节点N的值
# BST的左子树和右子树也都是 BST
# 我们如果在搜索时充分利用BST的性质，就能够有效剪枝。

# 算法流程
# 从根节点root开始，遍历整棵树
# 如果root等于p或q，那么root即为p和q的LCA。
# 如果root同时大于p和q，说明p和q 都在左子树上，那么将root.left作为根节点，继续第一步的操作。
# 如果root同时小于p和q，说明p和q 都在右子树上，那么将root.right作为根节点，继续第一步的操作。
# 如果以上情况都不成立，说明p和q分别在两颗子树上，那么root就是p和q的LCA。

# 复杂度分析
# 时间复杂度：O(N)，其中 N 为 BST 中节点的个数。在最坏的情况下，BST退化成链表，我们可能访问 BST 中所有的节点。
# 空间复杂度：O(N)，其中 N 为 BST 中节点的个数。所需开辟的额外空间主要是递归栈产生的，在最坏的情况下，BST退化成链表，那么递归栈的深度就是BST的节点数目。


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # root 等于 p或q
        if root == p or root == q:
            return root
        # p, q 都在左子树
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p, q 都在右子树
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # p, q 分别在左右子树，那么root即为结果
        return root