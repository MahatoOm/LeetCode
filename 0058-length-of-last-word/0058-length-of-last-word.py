class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        st = s.split(" ")
        print(st)
        for word in range(len(st)-1, -1, -1):
            if st[word]:
                return len(st[word])
        return 0