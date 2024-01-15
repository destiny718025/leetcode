# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root: Optional[TreeNode], low: int, high: int, num: int) -> int:
            if not root:
                return num
            if low <= root.val and root.val <= high:
                num += root.val
                num = dfs(root.left, low, high, num)
                num = dfs(root.right, low, high, num)
            elif root.val > high:
                num = dfs(root.left, low, high, num)
            elif root.val < low:
                num = dfs(root.right, low, high, num)

            return num

        return dfs(root, low, high, 0)