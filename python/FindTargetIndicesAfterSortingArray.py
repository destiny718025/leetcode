class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid - 1
                right = mid + 1
                while left >= 0 and nums[mid] == nums[left]:
                    res.append(left)
                    left -= 1
                res.append(mid)
                while right < len(nums) and nums[mid] == nums[right]:
                    res.append(right)
                    right += 1
                res.sort()
                return res
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res