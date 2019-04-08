class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        s = list(filter(str.isalnum, s.lower()))
        print(s)
        return True if s == s[::-1] else False

s = Solution()
s.isPalindrome("A man, a plan, a canal: Panam")
