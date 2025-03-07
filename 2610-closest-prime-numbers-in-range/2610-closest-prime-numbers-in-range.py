class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        num1 = -1
        num2 = -1
        if left == 1:
            left +=1
         

        prime = {idx : True for idx in range(left, right+1) }
        # print(prime)

        p = 2
        while p * p <= right:

            for i in range(p*p, right+1, p):
                if i in prime and prime[i]:
                    del prime[i]



            p += 1

        prime = list(prime.keys())
        # print(prime)
        prev_num = prime[0] if prime else 0
        # print(prev_num)
        min_dist = right

        for idx in range(len(prime) -1):
            distance = prime[idx+1] - prime[idx] 
            if distance < min_dist:
                num1 = prime[idx]
                num2 = prime[idx+1]
                min_dist = distance

        return [num1, num2]