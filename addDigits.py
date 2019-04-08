class Solution:
    def addDigits(self, num: int) -> int:
        #如果num为9的倍数，则结果为9。否则为num%9的余数
        return num and (num % 9 or 9)

s = Solution()
print(s.addDigits(38))