class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # result = 0
        # for  i in range(len(dominoes)):
        #     for j in range(i+1, len(dominoes)):
        #         if (dominoes[i] == dominoes[j]) or  (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0] ):
        #             result += 1

        # return result


        result = 0
        hash_map = {}
        for x , y in dominoes:
            if (x,y) in hash_map:
                result += hash_map[(x,y)] 
                hash_map[(x,y)] += 1
            elif (y,x) in hash_map:
                result += hash_map[(y,x)] 
                hash_map[(y,x)] += 1
            else:
                hash_map[(x,y)] = 1

        return result
