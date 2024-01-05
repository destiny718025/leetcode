class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, zero = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                zero += 1
            elif zero > 0:
                nums[i], nums[i - zero] = nums[i - zero], nums[i]

            i += 1