# 128. 哈希函数
# 中文English
# 在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：
#
# hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE
#
#                               = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
#
#                               = 3595978 % HASH_SIZE
#
# 其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。
#
# 给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。
#
# 样例
# 样例 1:
#
# 输入:  key = "abcd", size = 1000
# 输出: 978
# 样例解释：(97 * 33^3 + 98*33^2 + 99*33 + 100*1)%1000 = 978
# 样例 2:
#
# 输入:  key = "abcd", size = 100
# 输出: 78
# 样例解释：(97 * 33^3 + 98*33^2 + 99*33 + 100*1)%100 = 78
# 说明
# 对于这个问题，您没有必要设计自己的哈希算法或考虑任何冲突问题，您只需要按照描述实现算法.

class Solution2:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here
        n = len(key)
        ans = 0
        for i in range(len(key)):
            ans += ord(key[i]) * 33 ** (n-1 - i)

        return ans % HASH_SIZE
#
# 取模过程要使用同余定理：
# (a * b ) % MOD = ((a % MOD) * (b % MOD)) % MOD
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans

#
# sol=Solution()
# sol.hashCode(key='abcd', HASH_SIZE=1000)