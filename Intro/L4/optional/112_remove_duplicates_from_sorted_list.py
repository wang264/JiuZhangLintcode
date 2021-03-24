# 112. Remove Duplicates from Sorted List
#
# Given a sorted linked list, delete all
# duplicates such that each element appear only once.
#
#
# Example 1:
# Input: null
# Output: null
#
# Example 2:
# Input: 1->1->2->null
# Output: 1->2->null
#
# Example 3:
# Input: 1->1->2->3->3->null
# Output: 1->2->3->null


from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        while prev and curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next

        return dummy.next

l = build_linked_list_from_array(vals=[1,1,2,3,3])
sol = Solution()
rslt = sol.deleteDuplicates(head=l)