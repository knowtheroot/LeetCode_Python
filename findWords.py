class Solution:
    def findWords(self, words: [str]) -> [str]:
        if len(words) == 0:
            return []
        line = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in range(len(line)):
            str = line[i]
            print(sorted(str))

        return []

s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))