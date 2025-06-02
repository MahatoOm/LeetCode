class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 0
        heap = []
        for i in range(len(ratings)):
            heapq.heappush(heap , (ratings[i] , i))
        rating_list = [0] * len(ratings)

        while heap:
            rate , node = heapq.heappop(heap)

            if node - 1 >= 0 and rating_list[node-1] and ratings[node] > ratings[node-1]:
                rating_list[node] = (rating_list[node-1] + 1) 
            if node + 1 < len(ratings) and rating_list[node + 1] and ratings[node] > ratings[node+1]:
                rating_list[node] = max(rating_list[node] , rating_list[node+1] + 1)
            if not rating_list[node]:
                rating_list[node] += 1
        print(rating_list)
        return sum(rating_list)