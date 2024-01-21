class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s = "#" + s
        nxt = [{} for _ in range(len(s))]
        for i in range(len(s) - 2, -1, -1):
            nxt[i] = nxt[i + 1].copy()
            nxt[i][s[i + 1]] = i + 1

        i, j = 0, 0
        for char in t:
            if char in nxt[i]:
                i = nxt[i][char]
                j += 1
            else:
                return len(t) - j

        return 0