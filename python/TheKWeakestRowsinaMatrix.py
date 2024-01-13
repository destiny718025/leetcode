class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row, col = len(mat), len(mat[0])
        rankArr = []

        for i in range(row):
            left, right = 0, col - 1
            while left <= right:
                mid = (left + right) // 2
                if mat[i][mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            rankArr.append([left, i])

        sortArr = sorted(rankArr)

        return [x[1] for x in sortArr[:k]]