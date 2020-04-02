# 104. 合并k个排序链表
# 中文English
# 合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。
#
# 样例
# 样例 1:
#     输入:   [2->4->null,null,-1->null]
# 	输出:  -1->2->4->null
#
# 样例 2:
# 	输入: [2->6->null,5->null,7->null]
# 	输出:  2->5->6->7->null


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

import heapq

ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        dummy = ListNode(-1)
        tail = dummy
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next