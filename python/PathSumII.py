# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], arr: List[int], s: int, targetSum: int):
            if not node:
                return None

            arr.append(node.val)
            s += node.val
            if not node.left and not node.right and s == targetSum:
                self.res.append(arr)
            dfs(node.left, arr.copy(), s, targetSum)
            dfs(node.right, arr.copy(), s, targetSum)

        dfs(root, [], 0, targetSum)
        return self.res