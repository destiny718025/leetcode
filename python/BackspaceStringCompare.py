class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sLen, tLen = len(s) - 1, len(t) - 1
        newS, newT = '', ''

        while sLen >= 0:
            m = 0
            while sLen >= 0 and (s[sLen] == '#' or m != 0):
                if s[sLen] == '#':
                    m += 1
                else:
                    m -= 1
                sLen -= 1
            if sLen >= 0:
                newS += s[sLen]
                sLen -= 1

        while tLen >= 0:
            m = 0
            while tLen >= 0 and (t[tLen] == '#' or m != 0):
                if t[tLen] == '#':
                    m += 1
                else:
                    m -= 1
                tLen -= 1
            if tLen >= 0:
                newT += t[tLen]
                tLen -= 1

        return newS == newT