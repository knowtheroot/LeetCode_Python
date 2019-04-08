class Solution:
    def climbStairs(self, n: int) -> int:
        #到达第 i 阶的方法总数就是到第 (i−1) 阶和第 (i−2) 阶的方法数之和
        #因为最后到达不是走1步就是走2步
        #数组res，第n-1步就是结果
        if n == 0:
            return 1
        if n == 1:
            return 1
        res = [1,2]
        for i in range(2,n):
            res.append(res[i-1]+res[i-2])
        return res[n-1]

s = Solution()
print(s.climbStairs(3))