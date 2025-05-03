class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        top_count = Counter(tops)
        bottom_count = Counter(bottoms)

        # print(top_count)
        # print(bottom_count)
        # tops_dict = defaultdict(list)
        # bottoms_dict = defaultdict(list)

        # for i in range(len(tops)):
        #     tops_dict[tops[i]].append(i)

        # for i in range(len(bottoms)):
        #     bottoms_dict[bottoms[i]].append(i)

        

        while top_count and bottom_count:

            key_t_max = max(top_count, key=top_count.get)
            key_b_max = max(bottom_count, key=bottom_count.get)
            

            if top_count[key_t_max] > bottom_count[key_b_max]:
                count = 0
                for i in range(len(tops)):
                    if tops[i] != key_t_max:
                        if bottoms[i] == key_t_max :
                            count += 1
                        else:
                            
                            del top_count[key_t_max]
                            break
                if count == len(tops) -  top_count[key_t_max]: 
                    return count
                        

            else:
                count = 0
                for i in range(len(bottoms)):
                    if bottoms[i] != key_b_max:
                        if tops[i] == key_b_max:
                            count += 1
                        else:
                            del bottom_count[key_b_max]
                            break
                

                if count == len(tops) -  bottom_count[key_b_max]: 
                    return count



        return -1