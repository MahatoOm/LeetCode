class Solution:
    def minimumLength(self, s: str) -> int:
        
        # only frequency matters no need to actually delete the element
        n = len(s) 
        for char in set(s):
            count = s.count(char)
            if count >= 3:
                if count % 2 ==1:
                    n = n - count + 1
                else:
                    n = n - count + 2 

        return n
