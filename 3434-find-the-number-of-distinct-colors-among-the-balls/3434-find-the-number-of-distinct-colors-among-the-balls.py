class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        ball_dict = {}
        second_dict = {} # to track colors holding how many num
        
        result = []
        i = 0

        for x,color in queries:
            
            if x in ball_dict:
                prev_color = ball_dict[x]
                second_dict[prev_color] -= 1 
               
                if second_dict[prev_color] == 0:
                    del second_dict[prev_color]
            
            ball_dict[x] = color

            second_dict[color] = second_dict.get(color, 0) + 1 
            co = len(second_dict)             
           
            result.append(co)
            # print(x,y)
            # print(seen_colors)
            # print(ball_dict, "--> " , i)

            # print(second_dict, "-->", i)
            # i += 1
        return result
