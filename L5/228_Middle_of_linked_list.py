"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None:
            return head
        
        fast=head
        slow=head
        
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow