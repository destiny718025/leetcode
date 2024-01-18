class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prevArr = self.getRow(rowIndex - 1)
        curArr = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            curArr[i] = prevArr[i] + prevArr[i - 1]

        return curArr