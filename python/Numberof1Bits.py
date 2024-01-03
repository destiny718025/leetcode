class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n:
            if n % 2:
                num += 1
            n //= 2
        return num