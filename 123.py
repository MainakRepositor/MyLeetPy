class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            a = stones.pop()
            b = stones.pop()
            if a != b: stones.append(abs(a-b))
            stones.sort()
            
        return stones[-1] if len(stones) else 0
