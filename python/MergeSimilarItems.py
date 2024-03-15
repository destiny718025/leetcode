class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = []
        mergeItem = items1 + items2
        d = dict()

        for value, weight in mergeItem:
            if value in d:
                d[value] += weight
            else:
                d[value] = weight

        for i in sorted(d):
            res.append([i, d[i]])

        return res