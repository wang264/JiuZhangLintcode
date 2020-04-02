class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0

        if len(A) <= 2:
            return max(A)

        # f[i] 表示前i家房子最多收益, 答案是 dp[n]
        # dp[i] = max(dp[i-1], dp[i-2] + A[i-1])
        dp = [0] * (len(A)+1)
        dp[0] = 0
        dp[1] = A[0]
        for i in range(2, len(A)+1):
            # f[i-1] ---> 不打劫 第i傢,
            # f[i-2] + A[i-1] ---> 打劫第i傢(雖然是A[i-1]但是代表第i傢）
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i-1])

        return dp[len(A)]