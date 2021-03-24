# 451. Swap Nodes in Pairs
# 中文English
# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example
# Example 1:
#
# Input: 1->2->3->4->null
# Output: 2->1->4->3->null
# Example 2:
#
# Input: 5->null
# Output: 5->null
# Challenge
# Your algorithm should use only constant space. You may not modify the values in the list,
# only nodes itself can be changed.

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        dummy = ListNode("dummy", head)
        prev = dummy
        while prev.next and prev.next.next:
            curr_1 = prev.next
            curr_2 = curr_1.next
            next_p = curr_2.next
            prev.next = curr_2
            curr_2.next = curr_1
            curr_1.next = next_p

            prev = prev.next.next

        return dummy.next


l = build_linked_list_from_array(vals=[1, 2, 3, 4, 5])
sol = Solution()
rslt = sol.swapPairs(head=l)
