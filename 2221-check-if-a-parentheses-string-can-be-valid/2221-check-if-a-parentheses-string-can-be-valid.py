class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        # if its odd no way we can balance parenthesis 
        # if start of locked is closed there is no element in begining to balance and vice versa
        if n % 2 ==1 or (locked[0] == "1" and s[0] == ")" ) or (locked[n-1] == "1" and s[n-1] == "("):
            return False


        # if there are even len of s and no 1 in locked wee can return true
        if '1' not in locked:
            return True

        # left to right parcement 
        
        open_count = 0 ## to track no of open in locked == 1 and s == '('
        flexible_count = 0 # to track locked[i] == 0 which can be altered to ( any )
        for i in range(n):
            
            if locked[i] == '1':  # if it is fixed 
                if s[i] == "(": # ands[i] is open parenthesis increase open_count by one and if closed ')' -1
                    open_count += 1    
                else:
                    open_count -= 1        
            else:
                flexible_count += 1

            if open_count < 0: # open_count can be negative if s[i] == ")" closed
                if flexible_count > 0: # it can be balanced by flexible it it is before else return False
                    flexible_count -=1
                    open_count += 1
                else:
                    return False

        # right to left parcement

        close_count = 0 # to track no of open in locked == 1 and s == ')'
        flexible_count = 0  # to track locked[i] == 0 which can be altered to ( any )
        for i in range(n-1, -1, -1):
            
            if locked[i] == '1': # if it is fixed 
                if s[i] == ")": # ands[i] is close parenthesis increase close_count by one and if open '(' -1
                    close_count += 1    
                else:
                    close_count -= 1        
            else:
                flexible_count += 1

            if close_count < 0: # close_count can be negative if s[i] == "(" closed
                if flexible_count > 0:  # it can be balanced by flexible it it is before else return False
                    flexible_count -=1
                    close_count += 1
                else:
                    return False


        
        return True
                     

        
        