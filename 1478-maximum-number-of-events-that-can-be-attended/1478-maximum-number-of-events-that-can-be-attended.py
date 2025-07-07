class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans


# class Solution:
#     def maxEvents(self, events: List[List[int]]) -> int:
#         check = [False]
#         events = sorted(events, key = lambda x: x[0])
#         print(events)
#         idx = 0
#         for st, ed in events:
#             if ed > len(check):
#                 check += [False] * (ed - len(check) )

#             while idx < ed and check[st-idx-1] :
#                 idx += 1
#             if idx  < ed :
#                 check[st-idx-1] = True

#         return check.count(True)