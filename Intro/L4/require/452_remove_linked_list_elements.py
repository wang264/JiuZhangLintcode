# 452. Remove Linked List Elements
# 中文English
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Example 1:
#
# Input: head = 1->2->3->3->4->5->3->null, val = 3
# Output: 1->2->4->5->null
# Example 2:
#
# Input: head = 1->1->null, val = 1
# Output: null

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here
        if head is None:
            return None
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head

        dummy = ListNode(-1, next=head)
        prev_node = dummy
        curr_node = head

        while curr_node is not None:
            if curr_node.val == val:
                next_node = curr_node.next
                prev_node.next = next_node
                curr_node = prev_node  # because the current node has been deleted, need to set curr_node

            prev_node = curr_node
            curr_node = curr_node.next

        return dummy.next


linked_list = build_linked_list_from_array([1, 2, 3, 3, 4, 5, 3])
sol = Solution()
rslt = sol.removeElements(head=linked_list, val=3)
