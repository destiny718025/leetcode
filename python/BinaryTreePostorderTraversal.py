# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left if root.left else root.right
            else:
                root = stack.pop()
                res.append(root.val)
                if stack and stack[-1].left == root:
                    root = stack[-1].right
                else:
                    root = None

        return res