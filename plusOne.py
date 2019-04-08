class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        if len(digits) == 0:
            return []
        tempStr = ""
        for i in range(len(digits)):
            tempStr = tempStr + str(digits[i])
        tempStr = str(int(tempStr)+1)
        res = []
        for item in tempStr:
            res.append(int(item))
        return res

s = Solution()
print(s.plusOne([1,2,3]))