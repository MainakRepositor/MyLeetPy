class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = [i for i in arr if arr.count(i) == 1]
        return "" if k > len(arr) else arr[k - 1]
