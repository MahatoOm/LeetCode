class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq

        heap = []
        for element in nums:
            heapq.heappush(heap, element)

        
        # print(nums)
        count = 0
        while len(heap) >= 2:
            pop1 = heapq.heappop(heap)
            pop2 = heapq.heappop(heap)
            
            if pop1 >= k:
                break
            count += 1
            heapq.heappush(heap, min(pop1,pop2)* 2 + max(pop1,pop2))


        return count

