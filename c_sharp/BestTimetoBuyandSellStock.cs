public class Solution {
    public int MaxProfit(int[] prices) {
        int diff = 0;
        int min = prices[0];

        for (int i = 1; i < prices.Length; i++) {
            if (min > prices[i]) {
                min = prices[i];
            } else {
                if (diff < prices[i] - min) {
                    diff = prices[i] - min;
                }
            }
        }

        return diff;
    }
}