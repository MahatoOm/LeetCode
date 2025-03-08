class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        s = list(s)

        # hash_map = set()
        n = len(s)
        store = ''
        slided_window =['a']+ s[:k-1]

        count = 0
        for i in range(0,n-k+1):
            
            slided_window.append(s[i+k-1])
            del slided_window[0]
            

            if len(set(slided_window)) == k :#and ''.join(slided_window) not in hash_map:
                # hash_map.add(''.join(slided_window))
                count +=1
            


        return count