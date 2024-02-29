class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num = 0
        extraEmptyBottles = 0
        emptyBottle = 0
        while numBottles:
            num += numBottles
            emptyBottle = numBottles + extraEmptyBottles
            numBottles = emptyBottle // numExchange
            extraEmptyBottles = emptyBottle % numExchange

        return num