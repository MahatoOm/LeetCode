from collections import defaultdict,deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dq = deque([root])
        store = defaultdict(list)
        
        path = []
        paths = []
        comp_level = 0
        if not root:
            return paths
            
        while dq:
            
            size = len(dq)
            path = []
            
            
            for i in range(size):
                node = dq.popleft()
                path.append(node.val)
            
            
            
                # store[level].append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            paths.append(path)

        
            
            
        return paths
            
        
        