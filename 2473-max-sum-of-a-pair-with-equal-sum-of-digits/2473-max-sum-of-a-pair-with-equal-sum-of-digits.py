class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nums.sort()
        # print(nums)

        om_dictionary = {}
        for i in range(len(nums)):

            data = nums[i]
            sum_data = 0
            for element in str(data):

                sum_data += int(element)

            if sum_data in om_dictionary:
                om_dictionary[sum_data].append(data)
            else:
                om_dictionary[sum_data] = [data]

         

        # print(om_dictionary)           
        output = -1
        sum_var = -1
        for arr in om_dictionary:
            if len(om_dictionary[arr]) >= 2:
                sum_var =  om_dictionary[arr][-1] + om_dictionary[arr][-2]

                output = max(output, sum_var)

        return output




