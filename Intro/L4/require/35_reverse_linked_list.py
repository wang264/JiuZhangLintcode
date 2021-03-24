# 35. Reverse Linked List
# 中文English
# Reverse a linked list.
#
# Example
# Example 1:
#
# Input: 1->2->3->null
# Output: 3->2->1->null
# Example 2:
#
# Input: 1->2->3->4->null
# Output: 4->3->2->1->null
# Challenge
# Reverse it in-place and in one-pass

from helperfunc import build_linked_list_from_array, ListNode


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


l = build_linked_list_from_array(vals=[1, 2, 3])
sol = Solution()
rslt = sol.reverse(head=l)
