class Solution:
    def longestPalindrome(self, s: str) -> int:
        totalNum = 0
        calOdd = False

        dict = Counter(s)
        for num in dict.values():
            if not num % 2:
                totalNum += num
            elif num % 2 and not calOdd:
                totalNum += num
                calOdd = True
            else:
                totalNum += (num - 1)

        return totalNum