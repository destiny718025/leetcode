class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        counterNums = Counter(nums)
        setNums = set(nums)

        for word in setNums:
            if 2 * word == target:
                res += (counterNums[word] * (counterNums[word] - 1))
            for word2 in setNums:
                if word == word2:
                    continue
                if word + word2 == target:
                    res += (counterNums[word] * counterNums[word2])

        return res