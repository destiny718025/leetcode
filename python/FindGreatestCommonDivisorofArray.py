class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(a:int, b:int) -> int:
            if b == 0:
                return a
            return GCD(b, a % b)
        minNum, maxNum = nums[0], nums[0]
        for num in nums:
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        return GCD(maxNum, minNum)