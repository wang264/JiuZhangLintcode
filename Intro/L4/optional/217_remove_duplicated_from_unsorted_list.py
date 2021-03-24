# 217. Remove Duplicates from Unsorted List
# 中文English
# Write code to remove duplicates from an unsorted linked list.
#
# Example
# Example 1:
#
# Input: 1->2->1->3->3->5->6->3->null
# Output: 1->2->3->5->6->null
# Example 2:
#
# Input: 2->2->2->2->2->null
# Output: 2->null
# Challenge
# (hard) How would you solve this problem if a temporary buffer is not allowed? In this case,
# you don't need to keep the order of nodes.

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """

    def removeDuplicates(self, head):
        # write your code here
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head

        have_seen = set()
        while curr is not None:
            if curr.val not in have_seen:
                have_seen.add(curr.val)
                prev = curr
                curr = curr.next
            else:
                next_ptr = curr.next
                prev.next = next_ptr
                curr = next_ptr

        return dummy.next


sol = Solution()
l = build_linked_list_from_array([1, 2, 1, 3, 3, 5, 6, 3])
sol = Solution()
rslt = sol.removeDuplicates(head=l)
