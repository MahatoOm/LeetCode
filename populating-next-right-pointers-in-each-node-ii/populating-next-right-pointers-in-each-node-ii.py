"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        

        
        
        if not root:
            return root
        dq = deque([root])
        while dq:

            size = len(dq)
            
            for i in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    
                if node.right:
                    dq.append(node.right)
                
                    
                node.next = dq[0] if i < size-1 else None
        return root          
        
#         leftmost = root
#         if not root:
#             return root
        
#         while leftmost:
#             head = leftmost
            
#             while head:
#                 #connection 1
#                 if head.left and head.right:
#                     head.left.next = head.right
#                 if head.left and not head.right and head.next:
#                     if head.next.left:
#                         head.left.next = head.next.left
#                     elif head.next.right:
#                         head.left.next = head.next.right
                    
                
                    
#                 if head.right and head.next:
#                     if head.next.left:
#                         head.right.next = head.next.left
#                     elif head.next.right:
#                         head.right.next = head.next.right
                        
                    
                
#                 head = head.next
            
            
            
#             if leftmost.left:
#                 leftmost = leftmost.left
#             if not leftmost.left and leftmost.right:
#                 leftmost = leftmost.right
            
        
        