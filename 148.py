class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = Counter()
        for i, n in enumerate(nums):
            if n == key and i + 1 < len(nums):
                c[nums[i + 1]] += 1
        return c.most_common(1)[0][0]
