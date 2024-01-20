class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sortArr = sorted(nums)

        for num in nums:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if sortArr[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            res.append(right + 1)

        return res