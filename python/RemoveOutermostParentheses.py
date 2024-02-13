class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        i = 0

        for char in s:
            if char == "(":
                i += 1
            else:
                i -= 1
            if i > 1 or (i == 1 and char == ")"):
                res += char

        return res