class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        # for a five letter string, rotate left=3 equal rotate right=2
        offset = (left - right)%len(str)
        
        A = str[0:offset]
        B = str[offset:]
        return B+A