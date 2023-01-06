class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = prev = 0
        for upper, p in brackets:
            if income >= upper:
                tax += (upper - prev) * p / 100
                prev = upper
            else:
                tax += (income - prev) * p / 100
                return tax
        return tax    
