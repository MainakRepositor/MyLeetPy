class Solution:
      def sortEvenOdd(self, A):
        A[::2], A[1::2] = sorted(A[::2]), sorted(A[1::2])[::-1]
        return A
