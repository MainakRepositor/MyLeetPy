class Solution:
    def sortArrayByParity(self, A):
        return [a for a in A if a % 2 == 0] + [a for a in A if a % 2]
