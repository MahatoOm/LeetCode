class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        if n == 1  and not (s[0] == "*"):
            return False 
        
        open_count = 0
        star_count = 0
        for i in range(n):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                open_count -=1
            else:
                star_count +=1


            if open_count < 0:
                if star_count > 0:
                    star_count -= 1
                    open_count += 1
                else:

                    print("cobra")
                    return False

        close_count = 0
        star_count = 0
        for i in range(n-1, -1, -1):
            if s[i] == ")":
                close_count += 1
            elif s[i] == "(":
                close_count -=1
            else:
                star_count +=1


            if close_count < 0:
                if star_count > 0:
                    star_count -= 1
                    close_count += 1
                else:
                    return False
     
        
        return  True