class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        #ch3cking if len is odd or even 
        '''
        Approach - 
        XOR (exclusive OR) has properties of 
            a ^ a = 0
            a ^ 0 = a
        Using, these properties
        So, our question is to pair with every element of num1 to every element to num2.

        for example, num1 = [ a, b], num2 = [c,d,e]

        after operations our result look like this,
            result = [(a^ c) ^ (a^d) ^ (a^e) ^ (b^c) ^ (b^d) ^ (b^e)]
        As, Xor is commutative,
            result = [ (a^a^a) ^ (b^b^b) ^ (c^c) ^ (d^d) ^(e^e) ]

            n1= len(nums1)
            n2 =len(nums2)
            result = [ (a ^a ^ ..... n2) ^ (b^b^ ....n2)
                        (c^c^.....n1) ^  (d^d^.....n1) ^  (e^e^.....n1) ]

            so, here is main idea, from properties of XOR,
            if a is even times [a ^ a ^ a ^ a] = 0,
            if a is odd times [a ^ a ^ a ] = a,


        '''

        len1 = len(nums1) % 2 # len1 is applicable for nums2 and vice versa
        len2 = len(nums2) % 2

        if len1 ==0 and len2 ==0 :
            result = 0

        elif len1 ==0 and len2 == 1:
            result = 0
            for num in nums1:
                result ^= num 
        elif len2 ==0 and len1 == 1:
            result = 0
            for num in nums2:
                result ^= num
        else:
            result = 0
            for num in nums1:
                result ^= num 
            for num in nums2:
                result ^= num

        return result




         # this has O(n^2) which exceeded time time so, we used some properties of XOR 

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         store = (nums1[i] ^ nums2[j])
        #         if i == 0 and  j == 0:
        #             output = store
        #         else:
        #             output = output ^ store


        # return output
            


