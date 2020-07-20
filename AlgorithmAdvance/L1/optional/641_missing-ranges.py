# 641. Missing Ranges
# 中文English
# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# Example
# Example 1
#
# Input:
# nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
# Output:
# ["2", "4->49", "51->74", "76->99"]
# Explanation:
# in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]
# Example 2
#
# Input:
# nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
# Output:
# ["4->6"]
# Explanation:
# in range[0,7],the missing range include range[4,6]


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        # 0 <= all element of nums <= 99
        rslt = []
        if len(nums) == 0:
            self.add_missing_range(left_num=lower, right_num=upper, rslt=rslt)
            return rslt

        self.add_missing_range(left_num=lower, right_num=nums[0] - 1, rslt=rslt)
        for i in range(len(nums) - 1):
            self.add_missing_range(left_num=nums[i] + 1, right_num=nums[i + 1] - 1, rslt=rslt)

        self.add_missing_range(left_num=nums[-1] + 1, right_num=upper, rslt=rslt)

        return rslt

    def add_missing_range(self, left_num, right_num, rslt):
        if left_num > right_num:
            pass
        elif left_num == right_num:
            rslt.append(str(right_num))
        else:
            rslt.append(f'{left_num}->{right_num}')


sol = Solution()
assert sol.findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99) ==["2", "4->49", "51->74", "76->99"]
assert sol.findMissingRanges(nums=[0, 1, 2, 3, 7], lower=0, upper=7) == ["4->6"]
assert sol.findMissingRanges(nums=[], lower=1, upper=1) == ['1']
