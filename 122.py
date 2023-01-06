class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        bucket, i = self._index(key)
        if i == -1:
            bucket.append([key,value])
            return
        bucket[i][1] = value

    def get(self, key: int) -> int:
        bucket, i = self._index(key)
        if i == -1:
            return -1
        return bucket[i][1]

    def remove(self, key: int) -> None:
        bucket, i = self._index(key)
        if i == -1: return
        bucket.pop(i)
        
    def _hash(self, key):
        return key % self.size
    
    def _index(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, [k,val] in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1
