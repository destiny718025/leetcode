public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            int num2 = target - nums[i];

            if (map.ContainsKey(num2)) {
                return new int[] {map[num2], i};
            }

            if (!map.ContainsKey(nums[i])) {
                map.Add(nums[i], i);
            }
        }

        return null;
    }
}