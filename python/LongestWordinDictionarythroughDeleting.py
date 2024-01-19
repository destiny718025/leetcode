class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for subStr in dictionary:
            if self.isSubsequences(s, subStr):
                if len(subStr) > len(res):
                    res = subStr
                elif len(subStr) == len(res) and subStr < res:
                    res = subStr

        return res

    def isSubsequences(self, s: str, sub: str) -> bool:
        i, j = 0, 0

        while i < len(sub) and j < len(s):
            if s[j] == sub[i]:
                i += 1
            j += 1

        return i == len(sub)