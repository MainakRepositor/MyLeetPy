class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr_b = [(bin(n)[2:].count('1'), len(bin(n)[2:]),n) for n in arr]
        arr_b.sort()
        return [n[2] for n in arr_b]
