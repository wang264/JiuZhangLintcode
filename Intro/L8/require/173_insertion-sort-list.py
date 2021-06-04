# 173 · Insertion Sort List
#
# Description
# Sort a linked list using insertion sort.
#
# Example
# Example 1:
# 	Input: 0->null
# 	Output: 0->null
#
#
# Example 2:
# 	Input:  1->3->2->0->null
# 	Output :0->1->2->3->null

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        # write your code here
        if not head:
            return None
        dummy = ListNode("dummy", head)

        prev = head # point to the last node that are sorted.
        curr = head.next  # the current node that need to be sorted.

        while curr:
            # if the current node is larger than the largest sorted node. then do nothing.
            if prev.val <= curr.val:
                prev = curr
                curr = curr.next
            else:
                # you want to insert a node in between start and start.next
                # so you want to find a node such that start.next is bigger than current.
                start = dummy
                while start.next.val <= curr.val:
                    start = start.next
                prev.next = curr.next
                curr.next = start.next
                start.next = curr

                # update the next node that need to work on
                curr = prev.next

        return dummy.next


l = build_linked_list_from_array(vals=[2, 1])
sol = Solution()
sol.insertionSortList(head=l)
