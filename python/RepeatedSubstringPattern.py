class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        string = ""

        i = 0
        while i < l // 2:
            string += s[i]
            mult = l // (i + 1)
            if string * mult == s:
                return True
            i += 1

        return False