class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idx = 0
        res = set()

        while idx < len(nums) - 2:
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                continue

            jdx = idx + 1
            kdx = len(nums) - 1

            while jdx < kdx:
                s = nums[idx] + nums[jdx] + nums[kdx]
                if s == 0:
                    res.add((nums[idx], nums[jdx], nums[kdx]))
                    while jdx < kdx and nums[jdx] == nums[jdx + 1]:
                        jdx += 1
                    while jdx < kdx and nums[kdx] == nums[kdx - 1]:
                        kdx -= 1
                    jdx += 1
                    kdx -= 1
                elif s < 0:
                    jdx += 1
                else:
                    kdx -= 1
            idx += 1
        return res