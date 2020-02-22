class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b

        partial_rslt = self.fastPower(a, b, n // 2)

        if n % 2 == 0:
            return (partial_rslt * partial_rslt) % b
        else:
            return (partial_rslt * partial_rslt * a) % b