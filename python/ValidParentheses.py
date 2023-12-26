class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i == '(':
                tmp.append(')')
                continue
            if i == '{':
                tmp.append('}')
                continue
            if i == '[':
                tmp.append(']')
                continue
            if not tmp or tmp.pop() != i:
                return False
        return not tmp