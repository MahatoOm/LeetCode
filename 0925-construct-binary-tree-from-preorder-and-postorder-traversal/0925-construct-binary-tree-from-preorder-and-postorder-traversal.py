# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder and postorder:
            root , _ = preorder.pop(0) , postorder.pop()

            len1 = postorder.index(preorder[0]) + 1 if postorder else 0

            return TreeNode(root, self.constructFromPrePost(preorder[:len1], postorder[:len1]) ,  self.constructFromPrePost(preorder[len1:], postorder[len1:]))



        