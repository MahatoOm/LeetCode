class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        broken = False
        count = 0
        for l in text:
            if l == " ":
                if  not broken:
                    count += 1
                broken = False
            else:
                if l in brokenLetters:
                    broken = True
        return count + 1 if not broken else count