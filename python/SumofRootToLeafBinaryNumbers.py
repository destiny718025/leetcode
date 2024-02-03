# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], num: int):
            if not node:
                return None

            num = num * 2 + node.val
            if not node.left and not node.right:
                self.sum += num
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        return self.sum