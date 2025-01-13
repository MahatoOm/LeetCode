class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # frquency_count = defaultdict(int)
        # for _, element in enumerate(nums):
        #     frquency_count[element] += 1 
            
        # left = 0
        # right = k

        # while left < k:

        #     count = max(frquency_count.keys())
            
        #     if frquency_count[count] < k:
        #         k -= frquency_count[count]
        #         del frquency_count[count]
        #     else:
        #         return count


# using natural property of heap, minheap as lowest element in front
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

