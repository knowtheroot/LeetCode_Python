class Solution:
    def majorityElement(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        ret = 0
        for i in range(len(nums)):
            num = nums[i]
            if count == 0:
                ret = num
            if ret != num:
                count -= 1
            else:
                count += 1
        return ret

s = Solution()
print(s.majorityElement([3,2,3]))