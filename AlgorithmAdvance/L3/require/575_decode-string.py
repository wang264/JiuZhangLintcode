# 575. Decode String
# 中文English
# Given an expression s contains numbers, letters and brackets.
# Number represents the number of repetitions inside the brackets(can be a string or another expression)．
# Please expand expression to be a string.
#
# Example
# Example1
#
# Input: S = abc3[a]
# Output: "abcaaa"
# Example2
#
# Input: S = 3[2[ad]3[pf]]xyz
# Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
# Challenge
# Can you do it without recursion?
#
# Notice
# Numbers can only appear in front of “[]”.

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        stack = []
        number = 0
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            else:
                if char == '[':
                    stack.append(number)
                    number = 0
                if char == ']':
                    # pop the stack until we see a number
                    temp_stack = []
                    while len(stack) > 0 and isinstance(stack[-1], str):
                        temp_stack.append(stack.pop())
                    temp_string = ''
                    while len(temp_stack) > 0:
                        temp_string += temp_stack.pop()
                    repeat = stack.pop()
                    stack.append(repeat * temp_string)
                elif char.isalpha():
                    stack.append(char)

        rslt = ''.join(stack)
        return rslt


sol = Solution()
sol.expressionExpand(s='3[abc]')
sol.expressionExpand(s='3[2[ad]3[pf]]xyz')


class SolutionRecursive:
    def expressionExpand(self, s):

        if not s or len(s) == 0:
            return s
        result, position = self.dfs(0, s, 0, '')
        return result

    def dfs(self, position, s, prev_num, prev_str):
        while position < len(s):
            while s[position].isdigit():
                prev_num = prev_num * 10 + int(s[position])
                position += 1

            if s[position] == "[":
                # reset the prev_str
                returned_str, ending_pos = self.dfs(position + 1, s, prev_num=0, prev_str="")
                # backtrack
                prev_str = prev_str + returned_str * prev_num
                position = ending_pos
                prev_num = 0
            # return the result
            elif s[position] == ']':
                return prev_str, position
            else:
                prev_str += s[position]
            position += 1
        return prev_str, position


solRec = SolutionRecursive()
assert solRec.expressionExpand(s='3[2[ad]3[pf]]xyz') == "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
