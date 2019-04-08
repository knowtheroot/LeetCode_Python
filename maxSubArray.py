class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        # if len(nums) <= 1:
        #     return nums[0]
        # sum = nums[0]
        # n = nums[0]
        # for i in range(1,len(nums)):
        #     print(sum)
        #     if n>0:
        #         n += nums[i]
        #     else:
        #         n = nums[i]
        #     #动态规划最主要的特征就是保留之前的计算结果，sum就是之前的计算结果
        #     if sum < n:
        #         sum = n
        # return sum
        if len(nums) == 0:
            return 0
        sum = nums[0]
        n = nums[0]
        for i in range(1,len(nums)):
            if n>0:
                n += nums[i]
            else:
                n = nums[i]
        if sum < n:
            sum = n
        return sum

s = Solution()
print(s.maxSubArray([-2,1,-3,-7]))