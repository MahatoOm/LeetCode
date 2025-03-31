class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)


        
        #for pos(idx) of k
        #we collect the sum of splitting point weights(x )+ weights(x+1) 
        pair_weight = [weights[i] + weights[i+1] for i in range(n-1)]

        #sorting to efficently calculate the final result
        pair_weight.sort()
        # print(pair_weight)

        #now, calculate the largest k-1 value and smallest k-1 values
        result = 0
        for i in range(k-1):
            result += pair_weight[n-2-i] - pair_weight[i]
        return result
            

            