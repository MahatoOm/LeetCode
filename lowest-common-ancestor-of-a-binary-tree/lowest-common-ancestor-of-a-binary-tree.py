# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        # Base case: if root is None or root is one of the nodes (p or q)
        if not root or root == p or root == q:
            return root
        
        # Recur on the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, this node is the LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null child (if one exists)
        return left if left else right

#         path = []
#         path_p = []
#         path_q = []
#         def dfs(node):
#             if not node:
#                 return
#             path.append(node)
#             print(path)
#             if node == p:
#                 path_p.append(path.copy()) 
#                 print(True)
#             if node == q:
#                 print(True)
#                 path_q.append(path.copy())
                
#             if node.left:
#                 node.left = dfs(node.left)
#                 path.pop()
                
#             if node.right:
#                 node.right = dfs(node.right)
#                 path.pop()
            
        
#         dfs(root)
#         print(path_p, "ghjk",path_q)
#         count = 0
        
#         for i , j in zip(path_p[0] , path_q[0]):
#             if i.val==j.val:
#                 count = i
#                 print(i.val)
        
#         return count.val