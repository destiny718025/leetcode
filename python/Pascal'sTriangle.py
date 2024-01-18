class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        for i in range(2, numRows + 1):
            arr = [1] * i
            for j in range(i):
                if j == 0 or j == i - 1:
                    continue
                arr[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(arr)

        return res