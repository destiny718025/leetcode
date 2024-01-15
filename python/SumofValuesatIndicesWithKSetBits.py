class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        dp = []
        kArr = []

        for i in range(len(nums)):
            if i == 0 or i == 1:
                num = i
            else:
                num = dp[i // 2] + i % 2
            dp.append(num)
            if num == k:
                kArr.append(i)

        return sum(nums[i] for i in kArr)