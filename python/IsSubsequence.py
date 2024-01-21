class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in s:
            i = t.find(char, i) + 1
            if not i:
                return False

        return True