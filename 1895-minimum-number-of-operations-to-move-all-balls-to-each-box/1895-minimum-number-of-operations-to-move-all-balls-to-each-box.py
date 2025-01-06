class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix_sum = [0] * (n)
        for i in range(n):
            
            if boxes[i] == "1":
                
                for j in range(n):
                    
                    prefix_sum[j] += abs(i-j)


        
            

        return prefix_sum
