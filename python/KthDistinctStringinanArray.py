class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countArr = Counter(arr)
        num = 0

        for word in arr:
            if countArr[word] == 1:
                num += 1
            if num == k:
                return word

        return ""