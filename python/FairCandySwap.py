class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        aliceSet = set(aliceSizes)
        bobSet = set(bobSizes)
        for aliceNum in aliceSet:
            bobNum = (bobSum - aliceSum + 2 * aliceNum) / 2
            if bobNum in bobSet:
                return [aliceNum, bobNum]