class Solution:
    def splitNum(self, num: int) -> int:
        numArr = [int(x) for x in str(num)]
        numArr.sort()
        num1, num2 = 0, 0

        i = 1
        while len(numArr):
            num1 += (i * numArr.pop())
            if len(numArr):
                num2 += (i * numArr.pop())
            i *= 10
        return num1 + num2