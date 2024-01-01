# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], num: int) -> int:
            if not root:
                return num

            left = dfs(root.left, num)
            right = dfs(root.right, num)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root, 0)
        return self.diameter
