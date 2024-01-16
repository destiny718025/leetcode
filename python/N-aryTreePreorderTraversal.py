"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            i = len(root.children) - 1
            while i >= 0:
                stack.append(root.children[i])
                i -= 1

        return res