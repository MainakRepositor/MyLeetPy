class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        difference = (sum(A) - sum(B)) / 2
        A = set(A)
        for candy in set(B):
            if difference + candy in A:
                return [difference + candy, candy]
