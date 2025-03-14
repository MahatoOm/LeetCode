class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        n = len(s)
        count = 0 
        #checking unique character
        for char in set(s):

            #find index of first and last occurance of char

            left = s.find(char)
            right = s.rfind(char)

            #find unique char between left and right index only if there exists

            if left< right:

                unique_char = set(s[left+1: right])
                count += len(unique_char)



            

                            
        return count
        

