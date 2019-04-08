class Solution:
    def largestPerimeter(self, A: [int]) -> int:
        if len(A) < 3:
            return 0
        A.sort()
        if len(A) == 3:
            if A[-2] + A[-3] > A[-1]:
                return A[-1] + A[-2] + A[-3]
        else:

        return 0

s = Solution()
print(s.largestPerimeter([3,6,2,3]))