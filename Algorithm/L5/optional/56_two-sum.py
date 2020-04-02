class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dic = {}
        for i, num in enumerate(numbers):
            if target - numbers[i] in dic.keys():
                return [dic[target - numbers[i]], i]
            else:
                dic[num] = i

sol = Solution()
sol.twoSum([2, 7 ,11, 15], 9)