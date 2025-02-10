class Solution:
    def clearDigits(self, s: str) -> str:

        s = list(s)
        # print(s)
        i = 0
        while True:

            if i == len(s):
                break

            if s[i].isdigit():
                if i == 0:
                    del s[i]
                    i -= 1
                else:
                    del s[i]
                    del s[i-1]
                    i -= 1
                    i -= 1
 
            i+=1
            
        return "".join(s)


'''
s = [['c', 'b', '3', '4']]
i =0, X
i = 1, X
i = 2, del 3 s = [['c', 'b', '4']] i = 1 del b s = [['c', '4']] i = 0
i = 1, del 4 s = [['c']]  i = 0 del 0 s = []  i =  -1
i = 0 s= []

'''