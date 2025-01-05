# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node:
                return True
            
            
            
            is_node_left = dfs(node.left)
            is_node_right = dfs(node.right)
            
            if is_node_left and is_node_right:
                

                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
                
                count +=1 
                return True
            return False
            
        if root:        
            dfs(root)
        return count