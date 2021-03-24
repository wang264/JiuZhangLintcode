# 174. Remove Nth Node From End of List
# 中文English
# Given a linked list, remove the nth node from the end of list and return its head.
#
# Example
# Example 1:
# 	Input: list = 1->2->3->4->5->null， n = 2
# 	Output: 1->2->3->5->null
#
#
# Example 2:
# 	Input:  list = 5->4->3->2->1->null, n = 2
# 	Output: 5->4->3->1->null
#
# Challenge
# Can you do it without getting the length of the linked list?
#
# Notice
# The minimum number of nodes in list is n.


from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        # if the length of linked list is 'n'.
        # we first set the fast and slow at dummy. so we need to let fast pointer move "n+1" step in advance.
        # so if we do this, when fast pointer is at the end(fast pointer=None), the slow pointer will point to the
        # previous node of the node we try to remove

        dummy = ListNode("dummy", head)
        fast = slow = dummy

        for i in range(n + 1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        prev = slow
        curr = slow.next

        prev.next = curr.next

        return dummy.next


linked_list = build_linked_list_from_array(vals=[1, 2, 3, 4, 5])

sol = Solution()
a = sol.removeNthFromEnd(head=linked_list, n=2)
