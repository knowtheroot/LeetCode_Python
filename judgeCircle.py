class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) == 0:
            return False

        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

s = Solution()
s.judgeCircle("UD")