class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        left, right = 0,0
        min_val = len(cards) + 1
        dict_table = {}
        while right < len(cards):
            if cards[right] in dict_table:
                idx = dict_table[cards[right]]
                min_val = min(min_val , right-idx + 1)


            dict_table[cards[right]] = right
            right+=1

        return min_val if min_val <= len(cards) else -1