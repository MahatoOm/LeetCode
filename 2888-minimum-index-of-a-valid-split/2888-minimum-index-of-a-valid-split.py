class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = Counter(nums)

        # this item has max num of occurence
        prev_freq = 0
        for data , freq in count.items():
            if freq > prev_freq:
                prev_freq = freq
                choosen_item = data

        
        left_counter = 0
        right_counter = prev_freq
        # print(count)
        # print(choosen_item)
        for i in range(len(nums)):
            if nums[i] == choosen_item:
                left_counter += 1
                right_counter -= 1

                if left_counter * 2 > i + 1 and right_counter * 2 > n - i - 1:
                    return i



        return -1 

            

