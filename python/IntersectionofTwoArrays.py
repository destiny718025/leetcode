class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = set()

        if len(set1) > len(set2):
            set1, set2 = set2, set1

        for num in set1:
            if num in set2:
                res.add(num)

        return res