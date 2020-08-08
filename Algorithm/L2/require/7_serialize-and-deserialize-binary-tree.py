# 7. Serialize and Deserialize Binary Tree
# 中文English
# Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

# Example
# Example 1:

# Input：{3,9,20,#,#,15,7}
# Output：{3,9,20,#,#,15,7}
# Explanation：
# Binary tree {3,9,20,#,#,15,7},  denote the following structure:
# 	  3
# 	 / \
# 	9  20
# 	  /  \
# 	 15   7
# it will be serialized {3,9,20,#,#,15,7}
# Example 2:

# Input：{1,2,3}
# Output：{1,2,3}
# Explanation：
# Binary tree {1,2,3},  denote the following structure:
#   1
#   / \
#  2   3
# it will be serialized {1,2,3}
# Our data serialization use BFS traversal. This is just for when you got Wrong Answer and want to debug the input.

# You can use other method to do serializaiton and deserialization.

# Notice
# There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.


from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        if root is None:
            return "#"

        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            if node is None:
                bfs_order.append("#")
            else:
                bfs_order.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ' '.join(bfs_order)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # None or ""
        data = deque(data.split(' '))
        if data[0] == '#':
            return None

        root = TreeNode(int(data.popleft()))
        q = deque([root])
        isLeft = True
        while q:
            curr_value = data.popleft()
            if curr_value != "#":
                curr_node = TreeNode(int(curr_value))
                q.append(curr_node)
                if isLeft:
                    q[0].left = curr_node
                else:
                    q[0].right = curr_node
            if not isLeft:
                q.popleft()
            isLeft = not isLeft

        return root

# Definition for a binary tree node.
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
    forest = [TreeNode(x) if x is not None else None for x in sequence ]

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


sol = Solution()
root = build_tree_breadth_first([3,9,20,None,None,15,7])
data = sol.serialize(root)
print(data)
root_2 = sol.deserialize(data)


data = sol.serialize(None)
root_3 = sol.deserialize(data)
