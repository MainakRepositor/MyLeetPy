class Solution:
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])
