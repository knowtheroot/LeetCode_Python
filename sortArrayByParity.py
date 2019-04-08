class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        if len(A) == 0:
            return []
        array1 = []
        array2 = []
        for i in range(len(A)):
            if A[i]%2 == 0:
                array1.append(A[i])
            else:
                array2.append(A[i])

        return array1+array2

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))