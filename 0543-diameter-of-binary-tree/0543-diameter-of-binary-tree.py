# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        def dfs(node):
            
            nonlocal diameter
            if not node:
                return 0
            
            

            left = dfs(node.left)
            right = dfs(node.right) 
            diameter = max(diameter,left + right)


            return max(left, right) + 1 




        
        dfs(root)

        return diameter

'''

Approach, question is to find longest disance between two nodes
longest distance = longest_left + longest_right

so, for this, we call dfs function for max_lenght from root.left and root.right and add 2(1+1) for root to left and root to right
'''