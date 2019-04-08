class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        #先排序，然后比较三个最大的正数和最小的两个负数及最大正数大乘积即可
        nums.sort()

        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

s = Solution()
print(s.maximumProduct([-1,-5,1,2,3]))