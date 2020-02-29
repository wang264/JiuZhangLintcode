class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    # the reason that after we reduce the problem to a two sum problem, left start from i+1 instead of 0 is
    # because we don't want to double count.
    # for example [-1,  0,  1,  2,  -1,  -4] one answer is [ -1, 0 ,1 ] we could have find this answer three times
    # for i=-1, i=0 and i=1 respectively

    # 先考虑2Sum的做法，假设升序数列a，对于一组解ai, aj, 另一组解ak, al
    # 必然满足 i < k j > l 或 i > k j < l, 因此我们可以用两个指针，初始时指向数列两端
    # 指向数之和大于目标值时，右指针向左移使得总和减小，反之左指针向右移 由此可以用
    # O(N) 的复杂度解决2Sum问题，3 Sum则枚举第一个数 O(N ^ 2)
    # 使用有序数列的好处是，在枚举和移动指针时值相等的数可以跳过，省去去重部分
    def threeSum(self, numbers):
        # write your code here
        if len(numbers) < 3:
            return []
        numbers.sort()
        rslt = []
        # reduce a + b + c =0 into a + b = -c
        for i in range(0, len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.find_two_sum(numbers, i + 1, len(numbers) - 1, -numbers[i], rslt)

        return rslt

    def find_two_sum(self, nums, left, right, target, rslt):
        while left < right:
            if nums[left] + nums[right] == target:
                rslt.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1