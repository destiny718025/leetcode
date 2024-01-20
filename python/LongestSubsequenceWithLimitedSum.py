class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        sumArr = []
        sumNum = 0

        for num in nums:
            sumNum += num
            sumArr.append(sumNum)

        for query in queries:
            left, right = 0, len(sumArr) - 1
            while left <= right:
                mid = (left + right) // 2
                if sumArr[mid] > query:
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(left)

        return res