class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        # find local for first occurrence
        first_occur = self.first_occurrence(nums=A, target=target)
        if first_occur == -1:
            return 0

        # iterate to count the number of element
        count = 1
        idx = first_occur + 1
        while idx < len(A) and A[idx] == target:
            count += 1
            idx += 1
        return count

    def first_occurrence(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:  # if equal we need to continue to search for the left part
                end = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

# sol = Solution()
# sol.totalOccurrence(A=[1,3,3,4,5], target=6)