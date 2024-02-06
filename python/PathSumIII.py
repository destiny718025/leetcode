# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], targetSum: int, total: int, isRoot: bool):
            if not node:
                return None
            total += node.val
            if total == targetSum:
                self.num += 1

            if node.left:
                dfs(node.left, targetSum, total, False)
                if isRoot:
                    dfs(node.left, targetSum, 0, True)
            if node.right:
                dfs(node.right, targetSum, total, False)
                if isRoot:
                    dfs(node.right, targetSum, 0, True)
            return None

        dfs(root, targetSum, 0, True)
        return self.num