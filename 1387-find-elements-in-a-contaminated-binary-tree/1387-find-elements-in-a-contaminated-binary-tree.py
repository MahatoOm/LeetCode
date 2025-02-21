# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.seen = set()
        self.bfs(root)

    def find(self, target: int) -> bool:
        # print(self.seen)
        return target in self.seen

    def bfs(self, root):
        
        stack = []
        stack.append(root)
        root.val = 0
        while stack:
            node = stack.pop()
            parent_val = node.val
            self.seen.add(parent_val)
            
            if node.left:
                node.left.val = (parent_val * 2) + 1
                stack.append(node.left)
            if node.right:
                node.right.val = (parent_val * 2) + 2
                stack.append(node.right)

        

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)