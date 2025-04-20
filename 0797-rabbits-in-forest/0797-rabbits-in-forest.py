class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        table = defaultdict(int)
        result = 0
        for idx, val in enumerate(answers):

            table[val] += 1

            # if val == table[val]:
            #     result += val
            #     table[val] -= val

        
        for key, val in table.items():
            
            diff = val - key
            if key ==0:
                result += val
            elif val > key :
                while val > key:
                    result += key + 1
                    val = val -  (key + 1) 
                    
                

                if val > 0:
                    result += key + 1

            else:
                result += key + 1
            
         

        return result 
                







