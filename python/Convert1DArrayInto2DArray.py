class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) != m * n:
            return res
        arr = []
        i = 0
        for num in original:
            arr.append(num)
            i += 1
            if i == n:
                res.append(arr)
                arr = []
                i = 0

        return res