# 36. Reverse Linked List II
# 中文English
# Reverse a linked list from position m to n.
#
# Example
# Example 1:
#
# Input: 1->2->3->4->5->NULL, m = 2 and n = 4,
# Output: 1->4->3->2->5->NULL.
# Example 2:
#
# Input: 1->2->3->4->NULL, m = 2 and n = 3,
# Output: 1->3->2->4->NULL.
# Challenge
# Reverse it in-place and in one-pass
#
# Notice
# Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(-1, head)
        m_prev = self.take_k_step(head=dummy, k=m - 1)
        n_next = self.take_k_step(head=dummy, k=n + 1)

        prev = n_next
        curr = m_prev.next
        for i in range(n-m + 1):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        m_prev.next = prev

        return dummy.next

    def take_k_step(self, head, k):
        curr = head
        for i in range(k):
            curr = curr.next

        return curr


arr = [1, 2, 3, 4, 5]

head = build_linked_list_from_array(arr)
sol = Solution()
rslt = sol.reverseBetween(head, m=2, n=4)
