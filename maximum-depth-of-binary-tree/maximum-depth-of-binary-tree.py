# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         def max_depth(node, depth,answer):
#             if not node:
#                 return
            
#             if not node.left and not node.right:
#                 answer = max(answer,depth)
                
#             # if node.left:
                
#             max_depth(node.left, depth + 1,answer)
#             # if node.right:
#             #     answer = max(answer, depth +1)
                
#             max_depth(node.right, depth +1,answer)
            
            
            
            
#         depth = 1
#         answer = 0
       
#         if root:
#             max_depth(root, depth,answer)
#         return answer


        def buttom_up(node):
            if not node:
                return 0
            left_param = buttom_up(node.left)
            right_param = buttom_up(node.right)
            
            return max(left_param , right_param) + 1
        
        return buttom_up(root)
            
        
    