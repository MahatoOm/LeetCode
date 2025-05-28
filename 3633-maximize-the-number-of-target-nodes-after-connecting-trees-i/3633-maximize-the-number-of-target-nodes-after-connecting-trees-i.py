# 
class Solution:
    
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        answer = [0] * n
        edge1_adjancy_list = defaultdict(list)
        edge2_adjancy_list = defaultdict(list)
        for i , j in edges1:
            edge1_adjancy_list[i].append(j) 
            edge1_adjancy_list[j].append(i) 
        for i , j in edges2:
            edge2_adjancy_list[i].append(j) 
            edge2_adjancy_list[j].append(i) 
        

        #for second node finding maximum k distance done which gonnaa added to final answer
        tree2_count = []
        for i in range(m):
            visited = set()
            count = self.DFS(edge2_adjancy_list , i , 0, k-1, visited )
            tree2_count.append(count) 
        max_tree2_dist = max(tree2_count)
   

        for i in range(n):
            visited = set()
            count = self.DFS(edge1_adjancy_list , i , 0, k, visited ) 
            answer[i] = (count + max_tree2_dist)


        return answer

    def DFS(self, adjancy_list , node , depth ,  move , visited ):

        if depth > move:
            return 0
        visited.add(node)
        count  = 1
        
        for neighbor in adjancy_list[node]:
            if neighbor not in visited:
                count += self.DFS(adjancy_list, neighbor, depth + 1, move , visited)
        return count

# from typing import List
# from collections import defaultdict

# class Solution:
#     def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
#         def build_graph(edges):
#             graph = defaultdict(list)
#             for u, v in edges:
#                 graph[u].append(v)
#                 graph[v].append(u)
#             return graph

#         def dfs(graph, node, depth, limit, visited):
#             if depth > limit:
#                 return 0
#             visited.add(node)
#             count = 1  # count this node
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     count += dfs(graph, neighbor, depth + 1, limit, visited)
#             return count

#         n = len(edges1) + 1
#         m = len(edges2) + 1

#         edge1_adj = build_graph(edges1)
#         edge2_adj = build_graph(edges2)

#         # For each node in tree2, compute reachable nodes within (k - 1)
#         tree2_counts = []
#         for i in range(m):
#             visited = set()
#             count = dfs(edge2_adj, i, 0, k - 1, visited)
#             tree2_counts.append(count)

#         max_reachable_in_tree2 = max(tree2_counts)
#         print(tree2_counts)

#         # For each node in tree1, compute reachable nodes within k
#         result = []
#         for i in range(n):
#             visited = set()
#             count = dfs(edge1_adj, i, 0, k, visited)
#             result.append(count + max_reachable_in_tree2)

#         return result
