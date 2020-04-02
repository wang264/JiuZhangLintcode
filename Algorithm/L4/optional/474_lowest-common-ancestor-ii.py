class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        path_A = self.get_path_to_root(A)
        path_B = self.get_path_to_root(B)

        ind_A = len(path_A) - 1
        ind_B = len(path_B) - 1

        while ind_A >= 0 and ind_B >= 0:
            if path_A[ind_A] != path_B[ind_B]:
                break
            else:
                LCA = path_A[ind_A]
                ind_A -= 1
                ind_B -= 1

        return LCA

    def get_path_to_root(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path