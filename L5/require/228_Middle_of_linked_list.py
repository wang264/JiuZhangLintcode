# # Definition of ListNode
# class ListNode(object):
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#     def __repr__(self):
#         return 'val:{} next:{}'.format(self.val, self.next.val if self.next else None)
#
#
# def build_linked_list_from_array(vals):
#     nodes = [ListNode(val) for val in vals]
#     for i in range(len(nodes)-1):
#         nodes[i].next = nodes[i+1]
#
#     return nodes[0]


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        # of the length is 0 or 1
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


#
# sol = Solution()
# head = build_linked_list_from_array([1,2,3,4,5,6])
#
# sol.middleNode(head)
#