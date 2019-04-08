class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return min(nums)
        nums.sort()
        return sum(nums[::2])

s = Solution()
print(s.arrayPairSum([7,3,1,0,0,6]))