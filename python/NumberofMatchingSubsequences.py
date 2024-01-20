class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        num = 0

        for word in words:
            flag = True
            i = 0
            for char in word:
                i = s.find(char, i) + 1
                if i == 0:
                    flag = False
                    break
            if flag:
                num += 1

        return num