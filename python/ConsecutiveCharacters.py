class Solution:
    def maxPower(self, s: str) -> int:
        maxNum = 0
        num = 0
        preChar = ""

        for char in s:
            if preChar != char:
                preChar = char
                num = 1
            else:
                num += 1

            maxNum = max(maxNum, num)

        return maxNum
