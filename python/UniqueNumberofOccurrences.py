class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set(arr)
        dict = {}

        for num in s:
            count = 0
            for n in arr:
                if n == num:
                    count += 1
            if count in dict:
                return False
            dict[count] = True
        return True