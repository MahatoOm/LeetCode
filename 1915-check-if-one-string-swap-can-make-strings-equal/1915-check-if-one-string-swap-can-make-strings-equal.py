class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        list1 = list(s1)

        list2 = list(s2)
        if s1 == s2:
            return True
        # HASHMAP to eashier acces
        s2_dict = defaultdict(list)
        not_matched = []
        for i in range(len(s1)):
            s2_dict[s2[i]].append(i)
            if list1[i] != list2[i]:
                not_matched.append(i)
            if len(not_matched) > 2:
                return False
        # print(not_matched)
        
        if len(not_matched) == 1:
                return False
        if len(not_matched) == 0:
                return True
        temp = list2[not_matched[0]]
        list2[not_matched[0]] = list2[not_matched[1]]
        list2[not_matched[1]] = temp
        return list1 == list2

        
        



        # count = 0 # at most 1 swap
        # pos = -1
        # for i in range(len(s2)):

        #     if list1[i] == list2[i]:
        #         continue
        #     if not s2_dict[list1[i]]:
        #         return False
        #     for  curr_pos in s2_dict[list1[i]]:
        #         if list1[curr_pos] != list2[curr_pos]:
        #             pos = curr_pos
        #     if pos == -1:
        #         return False
        #     temp = list2[i]
        #     list2[i] = list2[pos]
        #     list2[pos] = temp
        #     return list1 == list2

    
            
            
