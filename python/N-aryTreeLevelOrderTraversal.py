"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]

        while queue:
            l = len(queue)
            tmpArr = []
            while l > 0:
                root = queue.pop(0)
                tmpArr.append(root.val)
                for child in root.children:
                    queue.append(child)
                l -= 1
            res.append(tmpArr)

        return res