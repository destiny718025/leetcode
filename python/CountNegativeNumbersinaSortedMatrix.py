class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num = 0

        right = n - 1
        for i in range(m):
            while right >= 0 and grid[i][right] < 0:
                right -= 1
            num += ((m - i) * (n - right - 1))
            n = right + 1

        return num