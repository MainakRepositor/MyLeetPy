class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index, smallest = -1, math.inf
        for i, (r, c) in enumerate(points):
            dx, dy = x - r, y - c
            if dx * dy == 0 and abs(dx + dy) < smallest:
                smallest = abs(dx + dy)
                index = i
        return index
