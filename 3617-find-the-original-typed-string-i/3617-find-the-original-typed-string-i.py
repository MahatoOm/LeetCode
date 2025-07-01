class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        cnt  = 1
        prev = word[0]
        for idx  in range(1, len(word)):
            if word[idx] == prev:
                cnt += 1
            else:
                if cnt > 1:
                    res += cnt-1
                cnt = 1
                prev = word[idx]
        return res + cnt - 1 if cnt > 1 else res