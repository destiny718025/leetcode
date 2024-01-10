# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def leftDepth(root: Optional[TreeNode]) -> int:
            d = 0
            while root:
                d += 1
                root = root.left
            return d

        def rightDepth(root: Optional[TreeNode]) -> int:
            d = 0
            while root:
                d += 1
                root = root.right
            return d

        ld = leftDepth(root.left)
        rd = rightDepth(root.right)

        if ld == rd:
            return 2 ** (ld + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
