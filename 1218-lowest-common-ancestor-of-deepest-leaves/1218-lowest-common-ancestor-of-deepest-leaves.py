# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
          
        def post_order_traversal(node, depth ):
            if not node:
                return 0, None
            left_depth, res_l = post_order_traversal(node.left , depth + 1)
            right_depth , res_r = post_order_traversal(node.right , depth + 1)


            if left_depth > right_depth:
                    
                return left_depth + 1 , res_l
            elif right_depth > left_depth:
                
                return right_depth +1 , res_r
            
            else:
                return left_depth + 1, node


        

        
        _, nod = post_order_traversal(root, 0)
        return nod



      