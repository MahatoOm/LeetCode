# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(bound = None):
            if not inorder or inorder[-1] == bound: return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(bound)
            return root

        return build()