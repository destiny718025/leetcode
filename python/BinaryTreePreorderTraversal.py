# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], res: List[int]) -> List[int]:
            if not root:
                return res
            res.append(root.val)
            res = dfs(root.left, res)
            return dfs(root.right, res)

        return dfs(root, [])