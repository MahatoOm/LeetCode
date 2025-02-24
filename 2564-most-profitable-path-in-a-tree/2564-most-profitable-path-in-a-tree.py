from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        edge_map = defaultdict(list)
        for x, y in edges:
            edge_map[x].append(y)
            edge_map[y].append(x)

        n = len(edges) + 1  # Number of nodes = Number of edges + 1

        # Step 1: Bob's Path to 0 (DFS)
        bob_path = [-1] * n  # Store the step at which Bob visits each node
        def bob_dfs(node, parent, depth):
            bob_path[node] = depth
            if node == 0:
                return True  # Found node 0
            for neighbor in edge_map[node]:
                if neighbor != parent and bob_dfs(neighbor, node, depth + 1):
                    return True
            bob_path[node] = -1  # Reset if this path does not reach 0
            return False

        bob_dfs(bob, -1, 0)

        # Step 2: Alice’s DFS and Profit Calculation
        max_profit = float('-inf')

        def alice_dfs(node, parent, depth, curr_profit):
            nonlocal max_profit

            # Compute Alice’s earnings at this node
            if bob_path[node] == -1 or depth < bob_path[node]:  # Alice gets full amount
                curr_profit += amount[node]
            elif depth == bob_path[node]:  # Alice and Bob split
                curr_profit += amount[node] // 2
            
            # If leaf node, update max_profit
            if len(edge_map[node]) == 1 and node != 0:
                max_profit = max(max_profit, curr_profit)
                return

            # Continue DFS
            for neighbor in edge_map[node]:
                if neighbor != parent:
                    alice_dfs(neighbor, node, depth + 1, curr_profit)

        alice_dfs(0, -1, 0, 0)

        return max_profit



# class Solution:
#     def __init__(self):
#         self.final_output = 0

#     def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
#         edge_map = defaultdict(list)
#         for x, y in edges:

#             edge_map[x].append(y)
#             edge_map[y].append(x)


#         n = len(edges) + 1 # no of nodes = no of edges + 1
#         def bob_dfs( bob, path):

#             if bob == 0:
#                 paths.append(path)
#                 return
#             if bob in bob_seen:
#                 return
#             bob_seen.add(bob)
#             next_node = edge_map[bob]
#             for element in next_node:
#                 if element not in bob_seen:
#                     bob_dfs(element , path + [element])

#         def alice_dfs(bob, alice, alice_path):

#             if bob in alice_seen and len(edge_map[alice]) == 1:
#                 alice_paths.append(alice_path)
#                 return
            
             
#             if alice in alice_seen:
#                 return
#             alice_seen.add(alice)

#             next_node = edge_map[alice]
#             for element in next_node:
#                 if element not in alice_seen:
#                     alice_dfs(bob, element,  alice_path + [element])
        
            

        
#         paths = []
#         path = [bob]
#         gates = [False] * n
#         bob_seen = set()
#         bob_dfs(bob, path)
#         print(paths, "paths")

#         alice = 0
#         alice_path = [alice]
#         alice_paths = []
#         alice_seen = set()
#         alice_dfs(bob, alice, alice_path)
#         print(alice_paths, "alice_path")

#         net_income = 0

#         # self.dfs(0, bob, amount, edge_map, gates, net_income)
#         return self.final_output

#     # def dfs(self,alice,  bob, amount, edge_map, gates, net_income):
        
#         # if bob == 0 :
#         #     return 
#         # if alice == edge_map[alice]:
#         #     return 


        


#         # alice_next_nodes = edge_map[alice]
#         # bob_next_nodes = edge_map[bob]

#         # print(alice_next_nodes, bob_next_nodes)


    

        




