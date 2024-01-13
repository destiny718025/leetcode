class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        num = 0

        for i in range(len(nums) - 1):
            tmpNum = target - nums[i]
            left, right = i + 1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if tmpNum > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            num += (right - i)

        return num
