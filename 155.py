class Solution:
    def findRelativeRanks(self, nums):
    sort = sorted(nums)[::-1]
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
    return map(dict(zip(sort, rank)).get, nums)
