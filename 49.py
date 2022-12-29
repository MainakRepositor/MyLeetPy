class Solution:
    def repeatedNTimes(self, A):
        return collections.Counter(A).most_common(1)[0][0]
