class MRUQueue:

    def __init__(self, n: int):
        self.MRU = [i for i in range(n+1)]

    def fetch(self, k: int) -> int:
        data = self.MRU[k]
        del self.MRU[k]
        self.MRU.append(data)
        return data


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)