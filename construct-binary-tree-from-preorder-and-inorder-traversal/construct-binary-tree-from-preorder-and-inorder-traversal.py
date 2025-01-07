# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def maketree(in_left, in_right):
            
            
            if in_left > in_right:
                return None
            if not preorder:
                return
            val = preorder.pop(0)
            root = TreeNode(val)
            
            # here root splits in left and right with index in left and right
            
            index = idx_map[val]
            root.left = maketree(in_left, index-1)
            
            root.right = maketree(index+1, in_right)
            
            return root
        
        idx_map = { val : idx for  idx, val in enumerate(inorder)}
        
        return maketree( 0, len(inorder)-1)