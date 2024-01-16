# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root: TreeNode, arr: List[int]) -> List[int]:
            if not root:
                return arr
            arr = inorder(root.left, arr)
            arr.append(root.val)
            return inorder(root.right, arr)

        inorderArr = inorder(root, [])
        head = node = TreeNode()
        for num in inorderArr:
            node.right = TreeNode(num)
            node = node.right
        return head.right