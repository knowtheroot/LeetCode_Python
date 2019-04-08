class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        if len(A) == 0:
            return []
        array1 = []
        array2 = []
        result = []
        for i in range(len(A)):
            if A[i]%2 == 0:
                array1.append(A[i])
            else:
                array2.append(A[i])

        while array1 and array2:
            result.append(array1.pop())
            result.append(array2.pop())
        return result

s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))