class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
            if len(strs) == 0:
                return ""
            if len(strs) == 1:
                return strs[0]
            #find max item and min item in array
            s1 = min(strs)
            s2 = max(strs)
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return s1[0:i]

            return s1

s = Solution()
# print(s.longestCommonPrefix(["flsower","flsow","flsight"]))
print(s.longestCommonPrefix(["c","c"]))