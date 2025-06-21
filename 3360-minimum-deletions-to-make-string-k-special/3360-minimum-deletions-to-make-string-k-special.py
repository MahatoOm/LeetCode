class Solution:
    def minimumDeletions(selfg, word: str, k: int) -> int:
        
        freq = Counter(word)
        print(freq)
        print(freq[-1])
        result = inf
        for key, val in freq.items():
            
            result = min(result , selfg.count_deletion(freq, val , k))

        return result

    def count_deletion(selfg,freq, fxd_occur, k):
        count = 0

        for key , val in freq.items():
            if val < fxd_occur :
                count += val
            elif val > fxd_occur + k:
                count += val - fxd_occur - k
             
            
        return count
