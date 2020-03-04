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
        rslt = []
        curr_ip = []
        num_dot_left = 3
        curr_idx = 0
        self.dfs_helper(s, num_dot_left, curr_ip, curr_idx, rslt)
        return sorted(rslt)

    def dfs_helper(self, s, num_dot_left, curr_ip, curr_idx, rslt):
        if num_dot_left == 0 and self.is_valid(s[curr_idx:]):
            curr_ip.append(s[curr_idx:])
            rslt.append('.'.join(curr_ip))
            curr_ip.pop()

        for num_char in range(1, 4):  # can choose 1,2 or 3 character
            if curr_idx + num_char < len(s) and self.is_valid(s[curr_idx:curr_idx + num_char]):
                curr_ip.append(s[curr_idx:curr_idx + num_char])
                self.dfs_helper(s, num_dot_left - 1, curr_ip, curr_idx + num_char, rslt)
                curr_ip.pop()

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
