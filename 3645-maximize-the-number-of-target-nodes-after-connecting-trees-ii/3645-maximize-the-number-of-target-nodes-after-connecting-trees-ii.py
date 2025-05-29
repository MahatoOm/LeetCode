# from collections import deque
# class Solution:
#     def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        

#         def buildGraph(edges):
#             graph = defaultdict(list)
#             for a, b in edges:
#                 graph[a].append(b)
#                 graph[b].append(a)
#             return graph

#         def BFS(adjancy_list, node, depth, type_odd_even):

#             queue = deque()
#             queue.append((node, depth))
#             count = 0
#             visited = set()
#             while queue:
#                 node , depth = queue.popleft()
#                 visited.add(node)
#                 if depth %2 == type_odd_even :
#                     count += 1
                
#                 for neighbor in adjancy_list[node]:
#                     if neighbor not in visited:
#                         queue.append((neighbor , depth + 1))
                 
#             return count


#         edges1_graph = buildGraph(edges1)
#         edges2_graph = buildGraph(edges2)
#         print(edges1_graph)


#         maximum_even_reacheable = 0
#         maximum_odd_reacheable = 0
#         tree2 = []
#         for  i  in range(len(edges2)+1):

#             count = BFS(edges2_graph, i, 1, 1)
#             tree2.append(count)
#             if count % 2:
#                 maximum_odd_reacheable = max(maximum_odd_reacheable , count)
#             else:
#                 maximum_even_reacheable = max(maximum_even_reacheable ,count)
#         print(tree2)


#         tree1 = []
#         result = []
#         for i in range(len(edges1)+1):
#             count = BFS(edges1_graph, i, 1, 0)
#             tree1.append(count)
#             result.append( count + max(tree2)  )
#         print(tree1)

#         return result

class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def dfs(node, parent, depth, children, color):
            res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = dfs(0, -1, 0, children, color)
            return [res, n - res]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        res = [0] * n
        for i in range(n):
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res
