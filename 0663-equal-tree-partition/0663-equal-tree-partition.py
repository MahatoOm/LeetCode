# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.con = False
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(node):

            if not node:
                return 0
            return node.val + DFS(node.left) + DFS(node.right)

        def check_DFS(node , target):

            if not node:
                return 0
           

            left = check_DFS(node.left , target)
            right = check_DFS(node.right , target)
            total = node.val + left + right
            
            if node != root and total == target:
                self.con = True

            return total


        total = DFS(root)
        print(total)
        if total % 2:
            return False
        target = total / 2
        check_DFS(root , target)
        return self.con