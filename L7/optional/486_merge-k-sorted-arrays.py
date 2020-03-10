# 486. Merge K Sorted Arrays
# 中文English
# Given k sorted integer arrays, merge them into one sorted array.
#
# 样例
# Example 1:
#
# Input:
#   [
#     [1, 3, 5, 7],
#     [2, 4, 6],
#     [0, 8, 9, 10, 11]
#   ]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Example 2:
#
# Input:
#   [
#     [1,2,3],
#     [1,2]
#   ]
# Output: [1,1,2,2,3]
# 挑战
# Do it in O(N log k).
#
# N is the total number of integers.
# k is the number of arrays.

#######################################################################
# using heap
import heapq


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # write your code here
        result = []
        heap = []
        for idx, array in enumerate(arrays):
            if len(array) == 0:
                continue
            # push the (element, which array, which element in that array)
            heapq.heappush(heap, (array[0], idx, 0))

        while len(heap):
            val, curr_array, idx_in_curr_array = heapq.heappop(heap)
            result.append(val)
            # still have next element in that array
            if idx_in_curr_array + 1 < len(arrays[curr_array]):
                heapq.heappush(heap, (arrays[curr_array][idx_in_curr_array + 1], curr_array, idx_in_curr_array + 1))

        return result


#########################################################################
# use divide and conquer
class Solution2:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        if len(arrays) == 1:
            return arrays[0]

        return self.merge_range_arrays(arrays, 0, len(arrays) - 1)

    # write your code here
    def merge_range_arrays(self, arrays, start, end):
        if start == end:
            return arrays[start]

        mid = (start + end) // 2
        left = self.merge_range_arrays(arrays, start, mid)
        right = self.merge_range_arrays(arrays, mid + 1, end)
        return self.merge_two_arrays(left, right)

    def merge_two_arrays(self, arr_1, arr_2):
        i = 0
        j = 0
        rslt = []
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] < arr_2[j]:
                rslt.append(arr_1[i])
                i += 1
            else:
                rslt.append(arr_2[j])
                j += 1
        while i < len(arr_1):
            rslt.append(arr_1[i])
            i += 1
        while j < len(arr_2):
            rslt.append(arr_2[j])
            j += 1
        return rslt

#
# nums = [[1, 3, 5, 7], [2, 4, 6], [0, 8, 9, 10, 11]]
#
# sol = Solution2()
# sol.mergekSortedArrays(arrays=nums)