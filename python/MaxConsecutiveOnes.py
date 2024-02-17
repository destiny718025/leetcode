class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        c = 0

        for num in nums:
            if not num:
                c = 0
            else:
                c += 1
            maxC = max(maxC, c)

        return maxC