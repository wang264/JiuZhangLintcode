#   13. Implement strStr()
# 中文English
# For a given source string and a target string, you should output the first index(from 0) of target string in source string.
#
# If target does not exist in source, just return -1.
#
# Example
# Example 1:
#
# Input: source = "source" ，target = "target"
# Output: -1
# Explanation: If the source does not contain the target content, return - 1.
# Example 2:
#
# Input:source = "abcdabcdefg" ，target = "bcd"
# Output: 1
# Explanation: If the source contains the target content, return the location where the target first appeared in the source.
# Challenge
# O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
#
# Clarification
# Do I need to implement KMP Algorithm in a real interview?
#
# Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.

class Solution:
    def strStr(self, source, target):
        """
        for each possible search position, we start the search for match. if we find it, return the position. if can not find it after iteration. return -1
        """
        if source is None or target is None  or len(source)<len(target): 
            return -1
        # i is the index of the position to start search
        for i in range(0,len(source) - len(target) + 1):
            
            #j is the idex of character in the target
            j=0
            while j < len(target):
                if target[j] != source[i+j]:
                    break
                j +=1 
            
            if j == len(target):
                return i
        
        return -1


class Solution2:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        len_s = len(source)
        len_t = len(target)
        if len_t == 0:
            return 0

            # for different starting point
        for i in range(0, len_s - len_t + 1):
            if source[i:i + len_t] == target:
                return i

        return -1