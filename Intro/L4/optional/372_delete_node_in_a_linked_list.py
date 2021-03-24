# 372. Delete Node in a Linked List
# 中文English
# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
#
# Example
# Example 1:
#
# Input:
# 1->2->3->4->null
# 3
# Output:
# 1->2->4->null
# Example 2:
#
# Input:
# 1->3->5->null
# 3
# Output:
# 1->5->null

class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if node is None:
            return None
        if node.next is None:
            return None

        node.val=node.next.val
        node.next = node.next.next