class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s.strip()) == 0:
            return 0
        array = s.split()
        lastCount = len(array)-1
        resStr = array[lastCount]

        return len(resStr)

s = Solution()
print(s.lengthOfLastWord("   "))