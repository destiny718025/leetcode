class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen, bLen = len(a) - 1, len(b) - 1
        carry = 0
        res = ''

        while aLen >= 0 or bLen >= 0 or carry:
            if aLen >= 0:
                carry += int(a[aLen])

            if bLen >= 0:
                carry += int(b[bLen])

            res = str(carry % 2) + res
            carry //= 2
            aLen -= 1
            bLen -= 1

        return res