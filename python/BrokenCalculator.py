class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target < startValue:
            return startValue - target

        num = 0

        while startValue != target:
            num += 1
            if startValue > target:
                return num + startValue - target - 1
            elif target % 2:
                target += 1
            else:
                target //= 2

        return num