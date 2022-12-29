class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        numHash = {}
        for idx, num in enumerate(nums):
            if num in numHash:
                for i in numHash[num]:
                    if (i * idx) % k == 0:
                        pairs += 1
                numHash[num].append(idx)
            else:
                numHash[num] = [idx]
        return pairs
