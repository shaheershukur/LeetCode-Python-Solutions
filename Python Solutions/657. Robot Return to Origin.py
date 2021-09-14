# LeetCode Problem Title : 657. Robot Return to Origin
# LeetCode Problem Link  : https://leetcode.com/problems/robot-return-to-origin/
# Solution Explanation   : https://youtu.be/a2dE7K14-MA

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        row = 0
        col = 0
        for move in moves:
            if move == "U":
                row += 1
            elif move == "D":
                row -= 1
            elif move == "L":
                col += 1
            elif move == "R":
                col -= 1

        return (row == 0) and (col == 0)
