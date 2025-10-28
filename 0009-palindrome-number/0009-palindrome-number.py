class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        lst = list(str(x))
        n = len(lst)
        print(list)
        for i in range(n//2):
            
            if lst[i] != lst[n-1-i]:
                return False
        return True
