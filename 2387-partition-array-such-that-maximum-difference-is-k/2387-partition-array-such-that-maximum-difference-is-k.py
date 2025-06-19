class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        for el in nums:
            added = False

            if res:
                
                ma, mi = res[-1]
                if ma >= el and el >= mi:
                    added = True
                    
                    
                if el  > ma :
                    if el - mi <= k:
                        res[-1][0] = el
                        added = True
                        
                    

                if el < mi:
                    if ma - el <= k :
                        res[-1][1] = el
                        added = True
                        

            if not res or not added :
                res.append([el,el])


        return len(res)
