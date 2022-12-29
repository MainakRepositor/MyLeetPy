class Solution:
	def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
		dic = collections.defaultdict(int)
		res = []
		for weight, value in items1:
			dic[weight] += value
		for weight, value in items2:
			dic[weight] += value
		for weight in sorted(dic.keys()):
			res.append([weight, dic[weight]])
		return res
