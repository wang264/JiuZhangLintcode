# 225. Find Node in Linked List
# 中文English
# Find a node with given value in a linked list. Return null if not exists.
#
# Example
# Example 1:
#
# Input:  1->2->3 and value = 3
# Output: The last node.
# Example 2:
#
# Input:  1->2->3 and value = 4
# Output: null
# Notice
# If there are multiple nodes of the same value return the first one.

from helperfunc import ListNode


class Solution:
    """
    @param: head: the head of linked list.
    @param: val: An integer.
    @return: a linked node or null.Imp
    """

    def findNode(self, head, val):
        # write your code here
        curr = head
        while curr is not None:
            if curr.val == val:
                return curr
            curr=curr.next

        return None
