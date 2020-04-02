class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1

        left = 0
        right = index

        while left + 1 < right:
            mid = (left + right) // 2
            if reader.get(mid) < target:
                left = mid
            else:
                right = mid

        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right

        return -1