

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        first_occur = self.find_first_occurrence(nums=A, target=target)
        if first_occur == -1:
            return [-1, -1]
        last_occur = first_occur
        while last_occur < len(A) and A[last_occur] == target:
            last_occur += 1

        return [first_occur, last_occur - 1]

    def find_first_occurrence(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

# sol = Solution()
# sol.searchRange(A=[1,2,3,4,5,5,5,6], target=5)