class Solution:
        def minOperations(self, nums: List[int]) -> int:
            cnt = prev = 0
            for cur in nums:
                if cur <= prev:
                    prev += 1
                    cnt += prev - cur
                else:
                    prev = cur
            return cnt
