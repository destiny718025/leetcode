class Solution:
    def judgeCircle(self, moves: str) -> bool:
        row, col = 0, 0

        for move in moves:
            if move == 'R':
                row += 1
            elif move == 'L':
                row -= 1
            elif move == 'U':
                col += 1
            else:
                col -= 1

        return not row and not col
