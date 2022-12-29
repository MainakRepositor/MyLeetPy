class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        mx = max(candies)
        return [c+extraCandies >=mx for c in candies]
