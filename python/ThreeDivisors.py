class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        num = 0
        for i in range(1, n + 1):
            if n % i == 0:
                num += 1
            if num > 3:
                return False
        return num == 3