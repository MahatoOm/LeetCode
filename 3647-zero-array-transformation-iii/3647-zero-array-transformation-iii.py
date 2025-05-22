class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)

'''
class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        



        heap = []
        for start , end in queries :
            heapq.heappush(heap, [start-end, start, end])

        print(heap)
        result = 0
        
        while heap :

            _ , st, ed = heapq.heappop(heap)
            used = False
            while st <= ed :

                if not nums[st]:
                    st+=1
                else:
                    nums[st] -= 1
                    used = True
                    st += 1
            if not used:
                result += 1
        return result if len(set(nums)) == 1 else -1

'''
