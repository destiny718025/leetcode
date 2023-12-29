# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid - 1) ^ isBadVersion(mid):
                return mid
            elif not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return n