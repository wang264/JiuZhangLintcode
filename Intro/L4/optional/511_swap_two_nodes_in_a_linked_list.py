# 511. Swap Two Nodes in Linked List
# 中文English
# Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, do nothing.
#
# Example
# Example 1:
#
# Input: 1->2->3->4->null, v1 = 2, v2 = 4
# Output: 1->4->3->2->null
# Example 2:
#
# Input: 1->null, v1 = 2, v2 = 1
# Output: 1->null
# Notice
# You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.


from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        dummy = ListNode("dummy", head)

        prev1, prev2 = self.find_previous(dummy, v1, v2)

        if prev1 is None or prev2 is None:
            return dummy.next

        if prev1 == prev2:
            return dummy.next

        if prev1.next == prev2:
            self.swap_adjacent(prev1)
        elif prev2.next == prev1:
            self.swap_adjacent(prev2)
        else:
            self.swap_remote(prev1, prev2)

        return dummy.next

    def find_previous(self, dummy, v1, v2):
        prev1, prev2 = None, None

        node = dummy
        while node.next is not None:
            if node.next.val == v1:
                prev1 = node
            if node.next.val == v2:
                prev2 = node
            node = node.next
        return prev1, prev2

    def swap_adjacent(self, prev):
        curr_1 = prev.next
        curr_2 = curr_1.next
        _next = curr_2.next

        curr_1.next = _next
        curr_2.next = curr_1
        prev.next = curr_2

    def swap_remote(self, prev1, prev2):
        curr_1 = prev1.next
        next_1 = curr_1.next

        curr_2 = prev2.next
        next_2 = curr_2.next

        prev1.next = curr_2
        curr_1.next = next_2
        prev2.next = curr_1
        curr_2.next = next_1


arr = [10, 8, 7, 6, 4, 3]
head = build_linked_list_from_array(vals=arr)
v1 = 7
v2 = 6

sol = Solution()
rslt = sol.swapNodes(head,v1,v2)
