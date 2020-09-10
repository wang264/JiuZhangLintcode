# 426. 恢复IP地址
# 给一个由数字组成的字符串。求出其可能恢复为的所有IP地址。
# (你的任务就是往这段字符串中添加三个点, 使它成为一个合法的IP地址. 返回所有可能的IP地址.)
# 样例 1:
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# 解释: ["255.255.111.35", "255.255.11.135"] 同样可以.
#
# 样例 2:
# 输入: "1116512311"
# 输出: ["11.165.123.11","111.65.123.11"]
# 注意事项
# 你可以以任意顺序返回所有合法的IP地址.


class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        # write your code here
        num_of_number_left = 4
        curr_path = []
        rslt = []
        self.dfs_helper(s, num_of_number_left, 0, curr_path, rslt)
        return rslt

    def dfs_helper(self, s, numbers_left, curr_index, curr_path, rslt):
        if numbers_left == 0:
            if curr_index == len(s):
                rslt.append('.'.join(curr_path[:]))
            return

        # length of 1,2,3 char
        for length in range(1, 4):
            idx_start = curr_index
            if idx_start+length > len(s):
                continue

            sub_string = s[idx_start:idx_start+length]
            if self.is_valid(sub_string):
                curr_path.append(sub_string)
                self.dfs_helper(s, numbers_left - 1, idx_start+length, curr_path, rslt)
                curr_path.pop()

    def is_valid(self, s):
        if len(s) == 0:
            return False
        if s[0] == '0':
            if len(s) == 1:  # '0' is ok
                return True
            else:  # '01' or '001' is not ok
                return False
        if 1 <= int(s) <= 255:
            return True
        else:
            return False


sol =Solution()
assert sol.restoreIpAddresses(s="25525511135") == ["255.255.11.135", "255.255.111.35"]
assert sol.restoreIpAddresses(s='1111') == ['1.1.1.1']
