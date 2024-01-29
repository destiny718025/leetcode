# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]

        while queue:
            l = len(queue)
            s = 0
            for i in range(l):
                root = queue.pop(0)
                s += root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(round(s / l, 5))
        return res