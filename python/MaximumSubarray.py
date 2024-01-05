class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        Sum = nums[0]

        for key in range(1, len(nums)):
            if Sum < 0:
                Sum = nums[key]
            else:
                Sum += nums[key]
            maxSum = max(maxSum, Sum)
        return maxSum