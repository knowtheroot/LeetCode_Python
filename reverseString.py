class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            print(s)
        print(s[::-1])
        return s[::-1]


s = Solution()
s.reverseString(["h","e","l","l","o"])