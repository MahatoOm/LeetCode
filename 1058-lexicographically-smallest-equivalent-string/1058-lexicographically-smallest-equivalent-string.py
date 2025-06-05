class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])  # Path compression
            return root[x]

        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:
                return
            if x_root < y_root:
                root[y_root] = x_root
            else:
                root[x_root] = y_root

        # Initialize parent for each character
        root = [i for i in range(26)]

        # Create unions based on s1 and s2
        for i in range(len(s1)):
            union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        # Build the result string
        result = ''
        for ch in baseStr:
            smallest_equiv_char = chr(find(ord(ch) - ord('a')) + ord('a'))
            result += smallest_equiv_char

        return result
