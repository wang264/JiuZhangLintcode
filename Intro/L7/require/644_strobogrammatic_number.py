# 644. Strobogrammatic Number
# 中文English
# A mirror number is a number that looks the same when rotated 180 degrees (looked at upside down).For example, the numbers "69", "88", and "818" are all mirror numbers.
#
# Write a function to determine if a number is mirror. The number is represented as a string.
#
# Example
# Example 1:
#
# Input : "69"
# Output : true
# Example 2:
#
# Input : "68"
# Output : false

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        # write your code here
        n = len(num)
        if n % 2 == 0:
            left = n // 2 - 1
            right = n // 2
        else:
            left = n // 2
            right = n // 2

        while left >= 0 and right < n:
            if num[left] == "6" and num[right] == "9" or num[left] == "9" and num[right] == "6":
                pass
            elif num[left] == num[right] and num[left] in ["1", "8", "0"]:
                pass
            else:
                return False

            left -= 1
            right += 1

        return True


sol = Solution()
sol.isStrobogrammatic(num="69")
sol.isStrobogrammatic(num="68")
