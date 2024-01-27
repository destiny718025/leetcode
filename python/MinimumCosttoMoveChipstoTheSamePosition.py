class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0

        for num in position:
            if num % 2:
                odd += 1
        return min(odd, len(position) - odd)