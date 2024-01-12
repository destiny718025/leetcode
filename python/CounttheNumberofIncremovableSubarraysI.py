class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        l = len(nums)
        num = 0

        for i in range(l):
            for j in range(i, l):
                prev = 0
                flag = True
                for k in range(l):
                    if i <= k and k <= j:
                        continue
                    flag = flag and (prev < nums[k])
                    prev = nums[k]
                if flag:
                    num += 1

        return num