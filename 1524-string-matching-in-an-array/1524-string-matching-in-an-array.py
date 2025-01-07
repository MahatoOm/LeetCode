class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        store = []
        for word in words:

            for data in words:
                if word == data:
                    continue

                if word in data and word not in store:
                    store.append(word)


        return store