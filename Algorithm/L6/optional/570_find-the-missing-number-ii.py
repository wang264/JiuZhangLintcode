# 570. 寻找丢失的数 II
# 给一个由 1 --- n 的整数随机组成的一个字符串序列，其中丢失了一个整数，请找到它。

# 样例1
# 输入: n = 20 和 str = 19201234567891011121314151618
# 输出: 17
# 解释:
# 19'20'1'2'3'4'5'6'7'8'9'10'11'12'13'14'15'16'18

# 样例2
# 输入: n = 6 和 str = 56412
# 输出: 3
# 解释:
# 5'6'4'1'2

# 注意事项
# n <= 30
# 数据保证有且仅有唯一解

class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        # write your code here
        used = {num: False for num in range(1, n + 1)}
        return self.find(n, str, 0, used)

    def find(self, n, str, idx, used):
        # we already split all the numbers
        if idx == len(str):
            # try to get the number that is not yet used.
            missing_numbers = []
            for key, val in used.items():
                if val is False:
                    missing_numbers.append(key)
            if len(missing_numbers) == 1:
                return missing_numbers[0]
            else:
                return None

        if str[idx] == '0':  # can not split anything start with zero
            return None

        for num_char in range(1, 3):  # can split 1 or 2 char
            num = int(str[idx:idx + num_char])
            if 1 <= num <= n and not used[num]:
                used[num] = True
                rslt = self.find(n, str, idx + num_char, used)
                if rslt:
                    return rslt
                used[num] = False

        return None


class Solution2:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        # write your code here
        used_number = set()
        return self.dfs_helper(n, 0, str, used_number)

    def dfs_helper(self, n, start_idx, str, used_number):
        if start_idx == len(str):
            for num in range(1, n + 1):
                if num not in used_number:
                    return num
        else:
            if str[start_idx] == '0':
                return None
            for num_of_char in range(1, 3): # we can parse 1 or 2 chars
                if start_idx + num_of_char > len(str):
                    continue
                parsed_int = int(str[start_idx:start_idx + num_of_char])
                if parsed_int in used_number or parsed_int > n:
                    continue
                used_number.add(parsed_int)
                rslt = self.dfs_helper(n, start_idx + num_of_char, str, used_number)
                if rslt is not None:
                    return rslt
                used_number.remove(parsed_int)


sol = Solution2()
sol.findMissing2(n=20, str="19201234567891011121314151618")
sol.findMissing2(n=12, str="1234567891011")
sol.findMissing2(n=6, str='56412')
