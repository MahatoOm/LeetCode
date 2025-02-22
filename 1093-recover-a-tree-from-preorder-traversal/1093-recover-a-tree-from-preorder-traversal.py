# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        
        n = len(traversal)
     # to count the current position in the list
        

      
        return self.build_tree(traversal , 0  )


    def build_tree(self, traversal, depth):
        if self.i >= len(traversal):
            return None
        count_of_dashes = 0 
        val = 0

        while self.i + count_of_dashes < len(traversal) and traversal[self.i+ count_of_dashes] == "-":
            count_of_dashes += 1
            
        if count_of_dashes != depth:
            return None
        self.i += count_of_dashes

        while self.i  < len(traversal) and traversal[self.i].isdigit():
            val = val * 10 +  int(traversal[self.i])
            self.i +=1

        node = TreeNode(val)

        node.left = self.build_tree(traversal, depth + 1)
        node.right = self.build_tree(traversal, depth + 1)

        
        return node



            