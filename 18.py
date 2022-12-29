class Solution:
	def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
		second = []
		res = 0
		for i in range(len(nums) - 1):
			for j in range(i + 1, len(nums)):
				if nums[j] - nums[i] == diff:
					second.append(j)
		for k, num in enumerate(nums):
			for j in second:
				if num - nums[j] == diff and k > j:
					res += 1
		return res

