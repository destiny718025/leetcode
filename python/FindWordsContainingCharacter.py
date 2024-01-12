class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        i = 0
        for string in words:
            if x in string:
                res.append(i)
            i += 1
        return res