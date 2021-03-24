# 483. Convert Linked List to Array List
# 中文English
# Convert a linked list to an array list.
#
# Example
# Example 1:
#
# Input: 1->2->3->null
# Output: [1,2,3]
# Example 2:
#
# Input: 3->5->8->null
# Output: [3,5,8]

from helperfunc import ListNode


class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """

    def toArrayList(self, head):
        # write your code here
        rslt = list()
        curr = head
        while curr is not None:
            rslt.append(curr.val)
            curr = curr.next
        return rslt
