class Solution:
    def largestSumOfAverages(self, nums: List[int], K: int) -> float:
        dp = [[0] * (K + 1) for _ in range(len(nums) + 1)]

        s = 0
        for i in range(1, len(nums) + 1):
            s += nums[i - 1]
            dp[i][1] = round(s / i, 5)

        for i in range(2, len(nums) + 1):
            for k in range(2, min(i, K) + 1):
                s = 0
                c = 0
                for j in range(i, k - 1, -1):
                    s += nums[j - 1]
                    c += 1
                    dp[i][k] = max(dp[i][k], dp[i - c][k - 1] + round(s / (i - j + 1), 5))

        return dp[len(nums)][K]