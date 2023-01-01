class Solution:
    def frequencySort(self, A):
        count = collections.Counter(A)
        return sorted(A, key=lambda x: (count[x], -x))
