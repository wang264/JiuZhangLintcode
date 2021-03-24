# 223. Palindrome Linked List
# 中文English
# Implement a function to check if a linked list is a palindrome.
#
# Example
# Example 1:
#
# Input: 1->2->1
# output: true
# Example 2:
#
# Input: 2->2->1
# output: false
# Challenge
# Could you do it in O(n) time and O(1) space?

from helperfunc import ListNode, build_linked_list_from_array


class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """

    def isPalindrome(self, head):
        # write your code here
        if head is None or head.next is None:
            return True
        middle_node = self.get_middle_node(head)
        head_second_part = middle_node.next
        reversed_second_part = self.reverse(head=head_second_part)
        return self.is_palindrome_helper(head,reversed_second_part)

    def is_palindrome_helper(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next

        return True
    def get_middle_node(self, head):
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow_ptr = dummy
        fast_ptr = dummy

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        return prev


arr = [1, 2, 3, 4, 4, 3, 2, 1]

head = build_linked_list_from_array(arr)
sol = Solution()
rslt = sol.isPalindrome(head=head)
