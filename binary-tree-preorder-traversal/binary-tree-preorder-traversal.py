# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        store = []
        
        def pre_order(node):
            store.append(node.val)
            
            if node.left:
                node.left = pre_order(node.left)
                
            if node.right:
                node.right = pre_order(node.right)
        if root:        
            pre_order(root)
        return store