# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        # stack = [(p,q)]

        # while stack:
        #     node1 , node2 = stack.pop()
        #     if node1.val != node2.val :
        #         return False
        #         break
        #     stack.append((p.left, q.left))
        #     stack.append((p.right, q.right))



        # return True


        def dfs(p , q):
            if not p and not q:
                return True
            

            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            
            
            return dfs(p.right , q.right) and dfs(p.left , q.left)
            
            if left and right:
                return True

       

        return dfs(p,q)