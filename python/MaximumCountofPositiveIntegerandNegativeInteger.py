class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        i, j = right, right + 1
        while j < len(nums) and nums[j] == 0:
            j += 1

        return max(i + 1, len(nums) - j)