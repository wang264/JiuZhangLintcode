# 685. First Unique Number in Data Stream
# 中文English
# Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the unique number is not found, return -1.
#
# Example
# Example1
#
# Input:
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 5
# Output: 3
# Example2
#
# Input:
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 7
# Output: -1
# Example3
#
# Input:
# [1, 2, 2, 1, 3, 4]
# 3
# Output: 3


class MyListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class DataStream:
    def __init__(self):
        # dictionary for each 'char', point to the previous node
        self.nums_to_prev = dict()
        # to record the duplicated chars, will be in this list after we see it the second time.
        self.dup_nums = set()
        self.dummy = MyListNode('.')
        self.tail = self.dummy

    def add(self, num):
        ######################################################
        # 第三次或以上見到，我們能直接判斷了
        if num in self.dup_nums:
            return

        ######################################################
        # 如果是第一次看到，我們加到鏈表中
        if num not in self.nums_to_prev:
            self.nums_to_prev[num] = self.tail
            node = MyListNode(num)
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
            return

        ######################################################
        # 第二次看到的時候，我們把Node從鏈表中刪除。如果那個節點是Tail的話，我們把Tail往前移。
        # delete the existing node
        if num in self.nums_to_prev:
            prev = self.nums_to_prev[num]
            prev.next = prev.next.next
            # if num is the last node.
            if prev.next is None:
                # tail node removed
                self.tail = prev
            else:
                self.nums_to_prev[prev.next.val] = prev

            self.nums_to_prev.pop(num)
            self.dup_nums.add(num)

    def _num_exist_in_linked_list(self, number):
        node = self.dummy.next
        while node:
            if node.val == number:
                return True
            node = node.next

        return False

    def first_unique_num_helper(self, number):
        if self._num_exist_in_linked_list(number) or number in self.dup_nums:
            return self.dummy.next.val
        else:
            return -1


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        # Write your code here
        ds = DataStream()
        for num in nums:
            ds.add(num)
            if num == number:
                break

        return ds.first_unique_num_helper(number)

