class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return ""
        array = (s[::-1].split())[::-1]
        res = ""
        for str in array:
            res = res+str+" "
        return res.strip()

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))