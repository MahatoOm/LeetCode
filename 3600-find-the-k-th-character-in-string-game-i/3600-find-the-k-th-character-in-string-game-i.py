class Solution:
    def kthCharacter(self, k: int) -> str:
        
        i = 0
        word = "a"
        alphabet = { "a" : "b", "b" : "c", "c":"d", "d":"e", "e":"f","f":"g", "g":"h","h": "i","i":"j", "j":"k", "k":"l", "l":"m", "m":"n", "n":"o" , "o":"p", "p":"q", "q":"r", "r":"s","s":"t" ,"t":"u", "u":"v","v":"w", "w":"x", "x" : "y", "y": "z", "z":"a"}
        while len(word) <= k:
            words = word
            for ch in words:
                word += alphabet[ch]


        return word[k-1]


