# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def top_down(node, depth):
            nonlocal max_depth
            if not node:
                return
            
            if not node.left and not node.right:
                max_depth = max(max_depth ,depth)
                
            # if node.left:
                
            top_down(node.left, depth + 1)
            # if node.right:
            #     answer = max(answer, depth +1)
                
            top_down(node.right, depth +1)
            
            
            
            
        max_depth = 0 
        
       
        if root:
            top_down(root, 1)
        return max_depth


#         def buttom_up(node):
#             if not node:
#                 return 0
#             left_param = buttom_up(node.left)
#             right_param = buttom_up(node.right)
            
#             return max(left_param , right_param) + 1
        
#         return buttom_up(root)
            
        
    