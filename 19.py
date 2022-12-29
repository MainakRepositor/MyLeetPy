class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n, sum_odd = len(arr), 0
        p_sum = [0] * ( n + 1)
        for i, a in enumerate(arr):
            p_sum[i + 1] = p_sum[i] + a
        for i, p in enumerate(p_sum):
            for j in range(i + 1, n + 1, 2):
                sum_odd += p_sum[j] - p_sum[i] 
        return sum_odd
