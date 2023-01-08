class NumArray:

	def __init__(self, nums: List[int]):
		self.nums = nums
		if len(self.nums) == 0:
			return None

		self.dp = [0]*(len(self.nums))
		s = 0
		j = 0
		for i in self.nums:
			s = s + i
			self.dp[j] = s
			j = j + 1

	def sumRange(self, i: int, j: int) -> int:
		if i == 0:
			return self.dp[j]
		return self.dp[j] - self.dp[i-1]
