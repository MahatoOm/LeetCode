class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        

        if abs(n - m) > 1 or (not s and not t ) or s == t:
            return False
        


        #for deletion 
        
        if n > m:
            j =0
            del_count = 0
            for i in  range(n):

                if j < n-1 and s[i] != t[j] :
                    del_count +=1
                else:
                    j+=1

                if del_count > 1:
                    return False
        elif n < m:
            add_count = 0
            j = 0
            for i in  range(m):

                if j < m-1 and t[i] != s[j] :
                    add_count +=1
                else:
                    j+=1

                if add_count > 1:
                    return False
        else:
            replace_count = 0
            j = 0
            for i in  range(m):

                if t[i] != s[j] :
                    replace_count +=1
                
                j+=1

                if replace_count > 1:
                    return False
                
        
        return True  
