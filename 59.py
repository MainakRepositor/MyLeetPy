class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            if op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
