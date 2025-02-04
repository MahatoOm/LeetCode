# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def bfs(root, sum_value,low, high):
            if not root:
                return 0
            
            
            stack = []
            stack.append(root)
            while stack:
                node = stack.pop()
                if low <= node.val <= high:
                    sum_value += node.val

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right) 

            return sum_value

        output = bfs(root, 0, low, high)
        return output




        