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
        # need to have a<=b<=c so prevent duplicate result.
        if len(numbers) < 3:
            return []
        numbers.sort()
        rslt = []
        # reduce a + b + c =0 into -a = b + c
        for i in range(0, len(numbers) - 2):
            # fix a
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            # find -a = b + c
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


class Solution2:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    # a+b+c = 0
    # 我们不想要重复答案。　所以我们规定a<b<c　不然的话答案会被重复寻找好多次。
    # 比如说  [-4, -2, 6]   [-2, 4, 6]
    def threeSum(self, numbers):
        # write your code
        numbers.sort()
        three_sum_rslts = []
        for i, num_3 in enumerate(numbers):
            if i < len(numbers)-1 and numbers[i] == numbers[i+1]:
                continue
            two_sum_rslts = self.two_sums(numbers, 0, i - 1, -1 * num_3)
            for two_sum_rslt in two_sum_rslts:
                two_sum_rslt.append(num_3)
                three_sum_rslts.append(two_sum_rslt)

        return three_sum_rslts

    def two_sums(self, sorted_list, idx_start, idx_end, target):
        left = idx_start
        right = idx_end
        rslt = []
        while left < right:
            two_sum = sorted_list[left] + sorted_list[right]
            if two_sum == target:
                rslt.append([sorted_list[left], sorted_list[right]])
                left += 1
                right -= 1
                while left < right and sorted_list[left - 1] == sorted_list[left]:
                    left += 1
                while left < right and sorted_list[right + 1] == sorted_list[right]:
                    right -= 1
            elif two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
        return rslt


sol = Solution2()
sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
sol.threeSum([1,0,-1,-1,-1,-1,0,1,1,1]) == [[-1, 0, 1]]
sorted(sol.threeSum([-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5])) == [[-100,1,99],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-1,5],[-4,0,4],[-4,1,3],[-3,-2,5],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,0,1]]




