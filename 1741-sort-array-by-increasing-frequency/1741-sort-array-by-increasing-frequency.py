class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = Counter(nums)
        # print(freq)
        freq = [(fre,val) for val, fre in freq.items()]
        freq.sort()
        # print(freq)
        # print(sorted_freq)
        res = []
        i = 0
        while i < len(freq):

            fre , val = freq[i]
            if i + 1 < len(freq) and freq[i+1][0] != fre:
                res += [val] * fre
                i += 1
                continue
            i+=1
            
            container = [val]
            while i < len(freq) and freq[i][0] == fre:
                container.append(freq[i][1])
                i+=1
            container.sort()
            container.reverse()
            for data in container:
                res += [data] * fre


        return res