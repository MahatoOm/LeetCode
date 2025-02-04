# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        #BFS iterative
        if not root:
            return 0
        sum_value = 0
        dq = collections.deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if low <= node.val <= high:
                sum_value += node.val

            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right) 

        return sum_value


        # Dfs Iterative
        # if not root:
        #     return 0
        
        # sum_value = 0
        # stack = []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     if low <= node.val <= high:
        #         sum_value += node.val

        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right) 

        # return sum_value




        