class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minSum = len(list1) + len(list2) - 2
        hashDict = {}
        res = []

        for i in range(len(list1)):
            hashDict[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in hashDict:
                if hashDict[list2[j]] + j == minSum:
                    res.append(list2[j])
                elif hashDict[list2[j]] + j < minSum:
                    minSum = hashDict[list2[j]] + j
                    res = [list2[j]]

        return res
