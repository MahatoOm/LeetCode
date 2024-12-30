# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        store = []
        
        def post_order(node):
            
            
            if node.left:
                node.left = post_order(node.left)
            if node.right:
                node.right = post_order(node.right)
            store.append(node.val)
            
        if root:        
            post_order(root)
        return store