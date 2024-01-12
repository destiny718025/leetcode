class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = []
        s = sorted(set(arr))
        hashS = dict()
        rank = 1
        for value in s:
            hashS[value] = rank
            rank += 1

        for value in arr:
            res.append(hashS[value])

        return res