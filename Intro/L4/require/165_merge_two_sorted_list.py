# 165. Merge Two Sorted Lists
# 中文English
# Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
#
# Example
# Example 1:
# 	Input: list1 = null, list2 = 0->3->3->null
# 	Output: 0->3->3->null
#
#
# Example 2:
# 	Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
# 	Output: 1->2->3->8->11->15->null

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode("dummy")
        curr_merged = dummy

        curr_1 = l1
        curr_2 = l2

        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                curr_merged.next = curr_1
                curr_1 = curr_1.next
            else:
                curr_merged.next = curr_2
                curr_2 = curr_2.next

            curr_merged = curr_merged.next

        if curr_1 is None:
            curr_merged.next = curr_2
        else:
            curr_merged.next = curr_1

        return dummy.next


l1 = build_linked_list_from_array([1, 3, 8, 11, 15])
l2 = build_linked_list_from_array([2])

sol = Solution()
rslt = sol.mergeTwoLists(l1, l2)
