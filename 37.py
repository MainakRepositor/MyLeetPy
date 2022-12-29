class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = collections.defaultdict(int)
        max_square = square_count = 0
        
        for a,b in rectangles:
            squares[min(a, b)] += 1
        
        for square, count in squares.items():
            if square > max_square:
                square_count = count
                max_square = square
            
        return square_count
