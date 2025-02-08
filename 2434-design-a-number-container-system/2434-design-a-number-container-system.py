import heapq
from collections import defaultdict
class NumberContainers:
    def __init__(self):
        # it stores index as key and value as value
        self.index_map = {}
        # use of sorted set in order to return smallest number in first place
        # it store which which index is placed in similar value
        self.value_map = defaultdict(SortedSet)
        
             

    def change(self, index: int, number: int) -> None:

        # if index has  already some value so we need to update value_map 
        if index in self.index_map:
            prev_value = self.index_map[index]

            
            self.value_map[prev_value].remove(index)
            # heapq.heappop(self.value_map[prev_value])
            if len(self.value_map[prev_value]) == 0:
                del self.value_map[prev_value]
        
        self.index_map[index] = number
        self.value_map[number].add(index)
    
        

    def find(self, number: int) -> int:
        # print(self.index_map)

        
        if number in self.value_map and self.value_map[number]:
            
            return self.value_map[number][0]
        
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)