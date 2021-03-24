# 113. Remove Duplicates from Sorted List II
# 中文English
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Example
# Example 1
#
# Input : 1->2->3->3->4->4->5->null
# Output : 1->2->5->null
# Example 2
#
# Input : 1->1->1->2->3->null
# Output : 2->3->null

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(-1, head)
        prev = dummy

        while prev.next and prev.next.next:
            if prev.next.val != prev.next.next.val:
                prev = prev.next
            else:
                # for example, if we have dummy -> 1 -> 2 -> 2 -> 2 -> 3
                # after this while loop we will have dummy -> 1 -> 2 -> 3, prev is point to '1'
                # but we still need to delete the last occourance of '2'
                while prev.next and prev.next.next and prev.next.val == prev.next.next.val:
                    prev.next = prev.next.next

                # still need to delete prev.next
                if prev.next is not None:
                    prev.next = prev.next.next

        return dummy.next


l = build_linked_list_from_array(vals=[1, 2, 3, 3, 4, 4, 5])
sol = Solution()
rslt = sol.deleteDuplicates(head=l)

a = "-14->-13->-12->-12->-11->-11->-11->-11->-11->-10->-10->-9->-9->-9->-8->-8->-7->-7->-6->-5->-5->-5->-5->-3->-3" \
    "->-3->-3->-2->-1->-1->-1->-1->0->0->0->1->1->1->1->1->2->2->2->3->3->3->3->4->4->5->5->6->6->6->6->7->7->8->8" \
    "->8->8->8->8->9->9->9->9->10->10->10->11->11->12->12->13->13->13->13->13->14->14->15->15->15->16->16->16->16" \
    "->17->17->17->17->18->18->18->18->19->19->21->21->21->22->23->24->25->25->25->25->25"
arr = [int(x) for x in a.split("->")]
l = build_linked_list_from_array(vals=arr)
sol = Solution()
sol.deleteDuplicates(head=l)

arr = [24, 25, 25, 25]
l = build_linked_list_from_array(vals=arr)
sol = Solution()
sol.deleteDuplicates(head=l)


