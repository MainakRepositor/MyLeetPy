class Solution:
	def subsetXORSum(self, nums: List[int]) -> int:
		subsets = [[]]
		res = 0
		for num in nums:
			for subset in subsets[:]:
				subsets.append(subset + [num])
		for subset in subsets:
			if subset:
				s = subset[0]
				for num in subset[1:]:
					s ^= num
				res += s
		return res
