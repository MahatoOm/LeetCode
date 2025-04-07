class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = ""


        for char in strs[0]:
            common += char
            l = 0
            while l < len(strs):
                if not strs[l].startswith(common):
                    return common[:-1]
                l+=1
                
        return common
