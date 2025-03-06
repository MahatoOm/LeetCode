class Solution:
    def minSwaps(self, data: List[int]) -> int:


        n = len(data)
        #total no of ones needed to be in one place
        count_of_one = data.count(1)

        # print(count_of_one)
        #variable to hold min swaps needed, initally assume total no of ones in data
        #Using sliding window
        slided = data[:count_of_one]
        
        swaps_needed_in_this_window = slided.count(0)
        min_swaps = swaps_needed_in_this_window 


        # - no of windows traversal needed = n - count of ones + 1
        for i in range(n-count_of_one):

            # slided_window = data[i:count_of_one+i] 
            if data[i] == 0:
                swaps_needed_in_this_window -= 1 #no of 0 presence in this window is swaps needed
            if data[count_of_one + i ] == 0 :
                swaps_needed_in_this_window += 1

            min_swaps = min(min_swaps, swaps_needed_in_this_window )



        return min_swaps
