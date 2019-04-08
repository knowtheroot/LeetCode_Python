class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = nums[i]
        if len(dict.keys()) < len(nums):
            return True
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,1]))