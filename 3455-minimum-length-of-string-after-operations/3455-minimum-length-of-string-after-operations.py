class Solution:
    def minimumLength(self, s: str) -> int:
        
        # only frequency matters no need to actually delete the element
        # store = list(s)


        n = len(s)
        # char_count = [] 
        for char in set(s):
            count = s.count(char)
            if count >= 3:
                if count % 2 ==1:
                    n = n - count + 1
                else:
                    n = n - count + 2 

                
                # left , right = s.find(char) , s.rfind(char)
                # store[left] = -1
                # store[right] = -1
        # if -1 in store:
        #     store = [char for char in store if char != -1]
            
        return n
