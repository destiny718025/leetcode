# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], targetSum: int, s: int) -> bool:
            if not root:
                return False
            s += root.val
            if s == targetSum and not root.left and not root.right:
                return True
            return dfs(root.left, targetSum, s) or dfs(root.right, targetSum, s)

        return dfs(root, targetSum, 0)