    def fillCups(self, A):
        return max(max(A), (sum(A) + 1) // 2)
