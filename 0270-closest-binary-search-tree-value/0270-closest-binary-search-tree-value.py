# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        node = root
        minimal_val = 10 ** 9
        output = 10 ** 9
        
        while node:
            if abs(target - node.val) == minimal_val:
                if output > node.val:
                    output = node.val
            
            if abs(target - node.val) < minimal_val:
                minimal_val = abs(target - node.val)
                output = node.val
            
            if target > node.val:
                node = node.right
                
            elif target <= node.val:
                node = node.left
                
                
        return output
        
        
        
        
        
        
        
#         return self.bfs(root, target)
        
#     def bfs(self, root, target):
#         if not root:
#             return
        
#         queue = collections.deque()
#         queue.append(root)
#         minimal_val = 10**9
#         output = 10 ** 9
        
#         while queue:
            
#             size = len(queue)
            
#             for i in range(size):
#                 node = queue.popleft()
                
#                 if abs(node.val - target) == minimal_val:
#                     if output > node.val:
#                         output = node.val

#                 if abs(node.val - target) < minimal_val:

#                     minimal_val = abs(node.val - target)    
#                     output = node.val


#                 if node.left:
#                     queue.append(node.left)
                    
#                 if node.right:
#                     queue.append(node.right)
                    
#         return output
                    
                    
                    
        
        
        
        