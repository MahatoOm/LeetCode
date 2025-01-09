class Solution:
    def isValid(self, s: str) -> bool:
        
        def check(ch):

            if ch == "(":
                return ")"
            elif ch == "{":
                return "}"
            elif ch == "[":
                return "]"


        stack = []
        if len(s) % 2==1:
            return False
        for i in range(len(s)):
          
            #push an opening char at top of the stack
            if s[i] == "(" or s[i] == "{" or s[i] == "[" :
                stack.append(s[i])
            

            if s[i] == ")" or s[i] == "}" or s[i] == "]" :
                if len(stack) >=1 and check(stack[-1]) == s[i]:   
               
                    stack.pop()
                else:
                    return False
          
        
        return True if len(stack) == 0 else False



            


