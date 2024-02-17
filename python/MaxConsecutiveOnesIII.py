class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxC, c = 0, 0
        curK = k
        numList = []
        countList = []

        preNum = 2
        for num in nums:
            if preNum != num:
                numList.append(preNum)
                countList.append(c)
                c = 0
            c += 1
            preNum = num

        if c > 0:
            numList.append(preNum)
            countList.append(c)

        c = 0
        for i in range(1, len(numList)):
            if not numList[i] and countList[i] > curK:
                curK = k
                c = 0
                continue
            elif not numList[i]:
                c += countList[i]
                curK -= countList[i]
            else:
                c += countList[i]
            for j in range(i + 1, len(numList)):
                if not numList[j] and countList[j] > curK:
                    c += curK
                    curK = 0
                    break
                elif not numList[j]:
                    c += countList[j]
                    curK -= countList[j]
                else:
                    c += countList[j]
            if curK > 0 and i > 1:
                if countList[i - 1] < curK:
                    curK = countList[i - 1]
                c += curK

            maxC = max(maxC, c)
            curK = k
            c = 0

        return maxC
