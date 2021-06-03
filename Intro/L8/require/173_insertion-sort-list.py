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

    def insertionSortList2(self, head):
        # write your code here
        if not head:
            return None
        dummy = None
        pass

    def insertionSortList(self, head):
        if not head:
            return head

        dummy_node = ListNode(-1, head)
        cur = head  # 当前已经拍好序的最后一个节点
        while cur.next:
            if cur.val <= cur.next.val:  # 如果下一个（待排）的节点比当前节点值大，不用进行插入
                cur = cur.next
            else:
                start = dummy_node  # 从头开始寻找插入位置，最终插入在start的后面
                while start.next.val <= cur.next.val:  # 当start的next的值比待排的大
                    start = start.next
                tmp = cur.next  # 将待排的节点取出
                cur.next = cur.next.next  # 更新待排节点
                tmp.next = start.next  # 插在start节点后面
                start.next = tmp

        return dummy_node.next


l = build_linked_list_from_array(vals=[1, 6, -1, 3, 0, -2, ])
sol = Solution()
sol.insertionSortList(head=l)


