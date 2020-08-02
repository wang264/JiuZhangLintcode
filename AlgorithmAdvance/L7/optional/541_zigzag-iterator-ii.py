# 541. Zigzag Iterator II
# 中文English
# Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases?
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to
#  you, replace "Zigzag" with "Cyclic".
#
# Example
# Example1
#
# Input: k = 3
# vecs = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9],
# ]
# Output: [1,4,8,2,5,9,3,6,7]
# Example2
#
# Input: k = 3
# vecs = [
#     [1,1,1]
#     [2,2,2]
#     [3,3,3]
# ]
# Output: [1,2,3,1,2,3,1,2,3]

from collections import deque


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """

    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = deque([deque(vec) for vec in vecs if len(vec)!=0])

    """
    @return: An integer
    """

    def next(self):
        # write your code here
        vec = self.queue.popleft()
        val = vec.popleft()
        if vec:
            self.queue.append(vec)
        return val

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        return len(self.queue) > 0


# Your ZigzagIterator2 object will be instantiated and called as such:


vecs = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
]
solution, result = ZigzagIterator2(vecs), []
while solution.hasNext(): result.append(solution.next())
# Output result
print(result)



vecs = [[],[]]

solution, result = ZigzagIterator2(vecs), []
while solution.hasNext(): result.append(solution.next())
# Output result
print(result)