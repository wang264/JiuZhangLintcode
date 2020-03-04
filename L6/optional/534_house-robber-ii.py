class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber2(self, A):
        # write your code here
        if not A:
            return 0

        if len(A) <= 2:
            return max(A)

        # f[i] 表示前i家房子最多收益, 答案是 dp[n]
        # dp[i] = max(dp[i-1], dp[i-2] + A[i-1])
        dp = [0] * (len(A) + 1)

        # case one: do not rob the last house
        dp[0] = 0
        dp[1] = A[0]
        for i in range(2, len(A)):  # skip the last hose
            # f[i-1] ---> 不打劫 第i傢,
            # f[i-2] + A[i-1] ---> 打劫第i傢(雖然是A[i-1]但是代表第i傢）
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])

        case_one_max = dp[len(A) - 1]

        # case two: do not rob the first house
        dp[1] = 0
        dp[2] = A[1]
        for i in range(3, len(A) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])

        case_two_max = dp[len(A)]

        return max(case_one_max, case_two_max)
