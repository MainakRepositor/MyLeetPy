class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i, n in enumerate(arr):
            if k <= n-i-1: return i+k
        return k+len(arr)
