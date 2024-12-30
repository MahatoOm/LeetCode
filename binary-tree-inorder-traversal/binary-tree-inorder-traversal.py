# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        store = []
        
        def in_order(node):
            
            
            if node.left:
                node.left = in_order(node.left)
            store.append(node.val)
            if node.right:
                node.right = in_order(node.right)
        if root:        
            in_order(root)
        return store