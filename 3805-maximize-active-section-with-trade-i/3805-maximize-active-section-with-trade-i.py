class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count_of_ones = s.count("1")
 
       
        first_zero = s.find("0")
        last_zero = s.rfind("0")
        left_count_of_ones = first_zero 
        right_count_of_ones = len(s) - last_zero - 1
        res = left_count_of_ones + right_count_of_ones
        if res == count_of_ones:
            return res
        rem_count_of_ones = count_of_ones - res
       
        left , right = first_zero , last_zero
        first_visit_of_one = False

        before_one = 0
        in_block_one = 0
        after_one = 0
        max_res_in_block = 0

        while left <= right and rem_count_of_ones > 0:
            
            if s[left] == '0':
                before_one += 1
                left += 1
            elif s[left] == "1":
                count = 0
                rem_count_of_ones -= 1
                left += 1
                
                
                in_block_one = 1
                while left <= right and s[left] == '1':
                    in_block_one += 1
                    left +=1
                    rem_count_of_ones -= 1
                

                after_one = 0
                while left <= right and s[left] == '0':
                    after_one += 1
                    left += 1

                max_res_in_block = max(max_res_in_block, before_one + after_one)
                before_one = after_one

        return count_of_ones + max_res_in_block
                




            