class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        '''
        using diskaktras algorithms
        using heap(priority queue) - time is our priority 
        we need shortest time to reach from 0 to n-1
        '''
    
        road_map = defaultdict(list)
        for i , j,  t in roads:
            
                road_map[i].append((j,t))
                road_map[j].append((i,t))

        # print(road_map)


        heap = [ (0 , 0) ] # time , current node
        visited = set() # it tracks the already visited cell
        shortest_time = [float("inf")] *n
        path_count = [0] * n

        shortest_time[0] = 0
        path_count[0] = 1
        MOD = 1_000_000_007
        while heap:
            current_time , current_node = heapq.heappop(heap)
            if current_time > shortest_time[current_node]:
                continue


            for next_node, t in road_map[current_node]:

                if t + current_time < shortest_time[next_node]:
                    shortest_time[next_node] = t + current_time
                    path_count[next_node] = path_count[current_node]
                    heapq.heappush(heap, (current_time+t, next_node))

                elif t + current_time == shortest_time[next_node]:
                    path_count[next_node] = (path_count[next_node] + path_count[current_node]) % MOD

        # print(time)
        return path_count[n-1]

                  
            




        '''
        # Time limit exceeded using dfs 

        
        start = 0
        end = n-1

        road_map = defaultdict(list)

        for i , j,  t in roads:
            road_map[i].append((j,t))
            road_map[j].append((i,t))
        # print(road_map)

        def check_paths(current_node, target_node, time, path):
            nonlocal result_map
            if current_node == target_node:
                result_map[time] += 1
                return
            

            for next_node, t in road_map[current_node]:
                if next_node not in path:
                    check_paths(next_node, target_node, time + t, path + [next_node])


            return




        result_map = defaultdict(int)
        path = []
        # paths = []
        # visites = set()
        check_paths(start, end, 0, path)
        min_time = min(result_map.keys())
        return result_map[min_time]


        '''