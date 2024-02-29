class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        res = []
        nums.sort()
        s = 0
        while s <= (total // 2):
            num = nums.pop()
            res.append(num)
            s += num

        return res