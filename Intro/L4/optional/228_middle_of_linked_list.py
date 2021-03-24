# 228. Middle of Linked List
# 中文English
# Find the middle node of a linked list.
#
# Example
# Example 1:
#
# Input:  1->2->3
# Output: 2
# Explanation: return the middle node.
# Example 2:
#
# Input:  1->2
# Output: 1
# Explanation: If the length of list is even return the center left one.
# Challenge
# If the linked list is in a data stream, can you find the middle without iterating the linked list again?

from helperfunc import ListNode


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow_ptr = dummy
        fast_ptr = dummy

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr
