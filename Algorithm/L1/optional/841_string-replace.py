# 841. String Replace
# 中文English
# Given two identical-sized string array A, B and a string S. All substrings A appearing in S are replaced by B.
# (Notice: From left to right, it must be replaced if it can be replaced. If there are multiple alternatives,
#  replace longer priorities. After the replacement of the characters can't be replaced again.)
#
# Example
# Example 1
#
# Input:
# A = ["ab","aba"]
# B = ["cc","ccc"]
# S = "ababa"
#
# Output: "cccba"
# Explanation: In accordance with the rules, the substring that can be replaced is "ab" or "aba". Since "aba" is
#  longer, we replace "aba" with "ccc".
# Example 2
#
# Input:
# A = ["ab","aba"]
# B = ["cc","ccc"]
# S = "aaaaa"
#
# Output: "aaaaa"
# Explanation: S does not contain strings in A, so no replacement is done.
# Example 3
#
# Input:
# A = ["cd","dab","ab"]
# B = ["cc","aaa","dd"]
# S = "cdab"
#
# Output: "ccdd"
# Explanation: From left to right, you can find the "cd" can be replaced at first, so after the replacement
# becomes "ccab", then you can find "ab" can be replaced, so the string after the replacement is "ccdd".
# Notice
# The size of each string array does not exceed 100, the total string length does not exceed 50000.
# The lengths of A [i] and B [i] are equal.
# The length of S does not exceed 50000.
# All characters are lowercase letters.
# We guarantee that the A array does not have the same string

class TrieNode:
  def __init__(self):
    self.replacement = None
    self.children = {}


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word, replacement):
    root = self.root
    for char in word:
      root = root.children.setdefault(char, TrieNode())
    root.replacement = replacement

  # 找到word前缀的最长replacement, 如果Trie中没有找到word的前缀, 那么返回word的
  # 第一个char(这样做的原因是为了表示从word的下一个char重新开始找)
  def search(self, word):
    root, replacement = self.root, None

    for char in word:
      if char not in root.children:
        break

      root = root.children[char]
      if root.replacement is not None:
        replacement = root.replacement

    if replacement is None:
      replacement = word[0]

    return replacement


# Trie
#
# O(k * (m + n))
#
# - k: a的长度
# - m: a中每个单词长度的平均值
# - n: s的长度
class Solution:
  """
  @param a: The A array
  @param b: The B array
  @param s: The S string
  @return: The answer
  """
  def stringReplace(self, a, b, s):
    if not a or not b:
      return s

    # 这一块代码整体: O(k * (m + n))
    trie = Trie()
    for i, word in enumerate(a): # O(k)
      # 只有word是s的子串其才会被放到trie中, 这样就保证了每次search的时候, 每次
      # 匹配s[i]做的都是有用功
      if word in s: # O(n)
        trie.insert(word, b[i]) # O(m)

    # 这一块代码整体: O(n)
    result = []
    while s:
      replacement = trie.search(s)
      result.append(replacement)
      s = s[len(replacement):]

    return "".join(result)

sol = Solution()
sol.stringReplace(a=["ab", "aba"], b=["cc", "ccc"], s="ababa")

sol.stringReplace(a=["cd", "dab", "ab"], b=["cc", "aaa", "dd"], s="cdab")
