class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n+1)
        self.ptr = 1

    def insert(self, pos: int, value: str) -> List[str]:
        self.stream[pos] = value
        res = []
        
        if pos == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
                
        return res
