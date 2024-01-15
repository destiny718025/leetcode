class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lMove, rMove, cMove = 0, 0, 0

        for move in moves:
            if move == 'L':
                lMove += 1
            elif move == 'R':
                rMove += 1
            else:
                cMove += 1

        return abs(lMove - rMove) + cMove