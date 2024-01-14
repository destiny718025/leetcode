class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            sum = (1 + mid) * mid / 2
            if sum == n:
                return mid
            elif sum > n:
                right = mid - 1
            else:
                left = mid + 1

        return right