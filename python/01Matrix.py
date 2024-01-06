class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        x, y = len(mat), len(mat[0])
        queue = deque()
        maxVal = x + y

        for i in range(x):
            for j in range(y):
                if mat[i][j] == 0:
                    queue.append([i, j])
                else:
                    mat[i][j] = maxVal

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            rx, ry = queue.popleft()
            for dx, dy in directions:
                row, col = rx + dx, ry + dy
                if 0 <= row < x and 0 <= col < y and mat[row][col] > mat[rx][ry] + 1:
                    mat[row][col] = mat[rx][ry] + 1
                    queue.append([row, col])

        return mat