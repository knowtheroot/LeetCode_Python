class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return None
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            #因为已经排序，所以判断大小来控制指针前进
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1

        return list(set(res))

s = Solution()
print(s.intersection([1,2,2,1], [2,2]))