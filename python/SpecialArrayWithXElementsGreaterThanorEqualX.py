class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        if nums[0] >= l:
            return l
        for i in range(1, l):
            num = l - i
            if nums[i] >= num and num > nums[i - 1]:
                return num
        return -1