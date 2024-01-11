class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def createFailArr(needle: str):
            l = len(needle)
            i, j = 1, 0
            failArr = [0]
            while i < l:
                if needle[i] == needle[j]:
                    failArr.append(j + 1)
                    i += 1
                    j += 1
                elif j == 0:
                    failArr.append(0)
                    i += 1
                else:
                    j = failArr[j - 1]
            return failArr

        failArr = createFailArr(needle)

        hLen = len(haystack)
        nLen = len(needle)
        i, j = 0, 0
        while i < hLen:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = failArr[j - 1]
            if j == nLen:
                return i - nLen

        return -1