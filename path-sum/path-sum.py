# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_val = []
        stack = []
        sumLeft = 0
        sumRight = 0
        
        
        def pre_order_traversal(root):
            nonlocal sum_val, sumLeft, sumRight
            if not root:
                return 
            node = root.val
            
            stack.append(node)
            # print(stack)
            
            if not root.left and not root.right:
                # print(stack)
                
                if sum(stack) == targetSum:
                    # print(True)
                    sum_val.append(True) 
                    return
            
            
            
            
            if root.left:
                pre_order_traversal(root.left)
                stack.pop()
            if root.right:
                pre_order_traversal(root.right)
                stack.pop()
        pre_order_traversal(root)
        return True if sum_val else False
        
            
            
            
            
            
        