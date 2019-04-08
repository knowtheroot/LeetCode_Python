class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            return None
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = int((low + high)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
        return None

s = Solution()
print(s.search([-1,0,3,5,9,12], 9))