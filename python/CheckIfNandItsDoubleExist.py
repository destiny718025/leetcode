class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr1 = []

        for _ in range(len(arr)):
            num = arr.pop(0)
            if num * 2 in arr or num * 2 in arr1:
                return True
            arr1.append(num)

        return False