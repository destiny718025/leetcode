class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pre = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if not pre:
                if nums[i] > nums[i - 1]:
                    pre = "in"
                else:
                    pre = "dec"
            else:
                if (pre == "in" and nums[i] < nums[i - 1]) or (pre == "dec" and nums[i] > nums[i - 1]):
                    return False

        return True