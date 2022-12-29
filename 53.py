class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                last = stack.pop()
                prices[last] = prices[last] - p
            stack.append(i)
        return prices
