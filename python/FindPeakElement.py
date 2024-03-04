class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid - 1

        return left