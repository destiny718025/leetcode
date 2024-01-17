# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num = 0
        self.deepest = 0
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], deep: int):
            if not root:
                return None
            deep += 1
            if deep > self.deepest:
                self.deepest = deep
                self.num = root.val
            elif deep == self.deepest:
                self.num += root.val
            dfs(root.left, deep)
            dfs(root.right, deep)

        dfs(root, 0)
        return self.num