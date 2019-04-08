class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        if len(A) == 0:
            return []
        for i in range(len(A)):
            A[i] = A[i] * A[i]

        print(A)
        return sorted(A)

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))