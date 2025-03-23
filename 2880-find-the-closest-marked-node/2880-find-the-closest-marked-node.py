class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        '''
        using heap priority queue 
        distance is our priority

        '''
        
        edge_map = defaultdict(list)
        for i, j, d in edges:
            edge_map[i].append((j,d))
        # print(edge_map)

        min_heap = [(0,s)]
        seen = set()
        while min_heap:
            cur_distance, cur_node = heapq.heappop(min_heap)
            seen.add(cur_node)
            if cur_node in marked:
                return cur_distance

            for neighbor, distance in edge_map[cur_node] :
                if neighbor not in seen:
                    heapq.heappush(min_heap, (cur_distance+distance , neighbor))




        return -1