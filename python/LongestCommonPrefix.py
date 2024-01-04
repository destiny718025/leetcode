class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        i = 0
        minLen = 200

        for string in strs:
            minLen = min(minLen, len(string))

        while i < minLen:
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return s
            s += char
            i += 1


        return s