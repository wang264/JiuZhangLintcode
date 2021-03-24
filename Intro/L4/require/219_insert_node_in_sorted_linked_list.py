# 219. Insert Node in Sorted Linked List
# 中文English
# Insert a node in a sorted linked list.
#
# Example
# Example 1:
#
# Input: head = 1->4->6->8->null, val = 5
# Output: 1->4->5->6->8->null
# Example 2:
#
# Input: head = 1->null, val = 2
# Output: 1->2->null

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """

    def insertNode(self, head: ListNode, val):
        if head is None:
            return ListNode(val)

        # write your code here
        dummy = ListNode(0, head)
        prev_ptr = dummy
        next_ptr = head

        while not (next_ptr is None or next_ptr.val > val):
            prev_ptr = next_ptr
            next_ptr = next_ptr.next

        curr_ptr = ListNode(val)
        prev_ptr.next = curr_ptr
        curr_ptr.next = next_ptr

        return dummy.next


linked_list = build_linked_list_from_array(vals=[1])
sol = Solution()
sol.insertNode(head=linked_list, val=0)
