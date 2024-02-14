class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        num = 0
        expected = sorted(heights)
        if expected == heights:
            return num

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                num += 1

        return num