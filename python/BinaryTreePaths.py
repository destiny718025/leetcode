# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node: Optional[TreeNode], arr: List[str]):
            if not node:
                return None
            arr.append(str(node.val))

            if not node.left and not node.right:
                self.res.append('->'.join(arr))
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.pop()
            return None

        dfs(root, [])
        return self.res