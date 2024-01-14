class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                res += str1[i]
            i += 1

        while len(res) > 0:
            if res * (len(str1) // len(res)) == str1 and res * (len(str2) // len(res)) == str2:
                return res
            res = res[:-1]

        return res