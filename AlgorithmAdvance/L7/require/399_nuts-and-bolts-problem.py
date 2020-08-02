# 399. Nuts & Bolts Problem
# 中文English
# Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping
# between nuts and bolts.
#
# Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be
# compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller. We will
# give you a compare function to compare nut with bolt.
#
# Using the function we give you, you are supposed to sort nuts or bolts, so that they can map in order.
#
# Example
# Given nuts = ['ab','bc','dd','gg'], bolts = ['AB','GG', 'DD', 'BC'].
#
# Your code should find the matching of bolts and nuts.
#
# According to the function, one of the possible return:
#
# nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG'].
#
# If we give you another compare function, the possible return is the following:
#
# nuts = ['ab','bc','dd','gg'], bolts = ['BC','AA','DD','GG'].
#
# So you must use the compare function that we give to do the sorting.
#
# The order of the nuts or bolts does not matter. You just need to find the matching bolt for each nut.
#

# 399. Nuts 和 Bolts 的问题
# 中文English
# 给定一组 n 个不同大小的 nuts 和 n 个不同大小的 bolts. nuts 和 bolts 一一匹配.
#
# 不允许将 nut 之间互相比较, 也不允许将 bolt 之间互相比较. 也就是说, 只许将 nut 与 bolt 进行比较,
# 或将 bolt 与 nut 进行比较. 我们会提供一个比较函数, 用于nut和bolt的比较.
#
# 利用我们提供的函数, 你需要将 nuts 或者 bolts 重新排列, 使得它们按照顺序一一匹配.
#
# Example
# 给出 nuts = ['ab','bc','dd','gg'], bolts = ['AB','GG', 'DD', 'BC']
#
# 你的程序应该找出bolts和nuts的匹配.
#
# 根据比较函数, 一组可能的返回结果是：
#
# nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG']
#
# 如果我们给你另外的比较函数，可能返回的结果是：
#
# nuts = ['ab','bc','dd','gg'], bolts = ['BC','AB','DD','GG']
#
# 因此的结果完全取决于比较函数，而不是字符串本身。因为你必须使用比较函数来进行排序。
#
# 各自的排序当中nuts和bolts的顺序是无关紧要的，只要他们一一匹配就可以。


"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Comparator:
    def cmp(self, nut, bolt):
        mapping = {k: v for k, v in zip([chr(a) for a in range(ord('A'), ord('Z') + 1)], range(1, 27))}
        if nut not in mapping.values() or bolt not in mapping.keys():
            return 2
        if nut > mapping[bolt]:
            return 1
        elif nut < mapping[bolt]:
            return -1
        else:
            return 0


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        n, m = len(nuts), len(bolts)
        if m != n:
            return
        # 通过快速排序的思想进行排序
        self.quickSort(nuts, bolts, compare, 0, n - 1)

    def quickSort(self, nuts, bolts, compare, start, end):
        if start >= end:
            return
        index = self.partition(nuts, bolts[start], compare, start, end)
        self.partition(bolts, nuts[index], compare, start, end)  # 找到匹配的bolt
        # 将bolts划分为两部分
        self.quickSort(nuts, bolts, compare, start, index - 1)
        self.quickSort(nuts, bolts, compare, index + 1, end)

    def partition(self, NorBs, pivot, compare, start, end):
        m, i = start, start + 1  # m表示枢轴的实际位置。 use the first element as pivot
        for i in range(m + 1, end + 1):  # 判断并且对nut和bolt通过交换进行排序
            if compare.cmp(pivot, NorBs[i]) == 1 or compare.cmp(NorBs[i], pivot) == -1:
                m += 1
                NorBs[m], NorBs[i] = NorBs[i], NorBs[m]
            elif compare.cmp(pivot, NorBs[i]) == 0 or compare.cmp(NorBs[i], pivot) == 0:
                # 在传统的QuickSort中，我们知道Pivot的位置，把第一个数字作为Pivot。
                # 可是现在我们不知道Pivot在哪儿，我们找到后先把真正的Pivot和第一个数换过来。
                # 再去重新看判断第一个数。
                NorBs[start], NorBs[i] = NorBs[i], NorBs[start]
                i -= 1
            else:
                continue

        NorBs[m], NorBs[start] = NorBs[start], NorBs[m]
        return m


sol = Solution()
nuts = [6, 10, 1, 2, 8, 9, 3, 5, 4, 7]
bolts = ['E', 'J', 'I', 'A', 'H', 'C', 'F', 'D', 'B', 'G']
sol.sortNutsAndBolts(nuts=nuts, bolts=bolts, compare=Comparator())
print(nuts)
print(bolts)
