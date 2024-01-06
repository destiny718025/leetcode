class Solution:
    def __init__(self):
        self.arr = []

    def quickSelect(self, a: int, b: int, k: int) -> int:
        pivot = self.arr[(a + b) // 2][0]

        i, j, t = a, b, a
        while t <= j:
            if self.arr[t][0] < pivot:
                self.arr[t], self.arr[i] = self.arr[i], self.arr[t]
                i += 1
                t += 1
            elif self.arr[t][0] > pivot:
                self.arr[t], self.arr[j] = self.arr[j], self.arr[t]
                j -= 1
            else:
                t += 1

        if i - a >= k:
            return self.quickSelect(a, i - 1, k)
        elif j - a + 1 >= k:
            return pivot
        else:
            return self.quickSelect(j + 1, b, k - (j - a + 1))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for x, y in points:
            self.arr.append([x ** 2 + y ** 2, x, y])

        kthDist = self.quickSelect(0, len(points) - 1, k)
        res = []

        for d, x, y in self.arr:
            if kthDist >= d:
                res.append([x, y])

        return res