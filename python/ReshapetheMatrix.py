class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        res = []
        x = 0
        arr = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr.append(mat[i][j])
                x += 1
                if x == c:
                    res.append(arr)
                    arr = []
                    x = 0

        return res