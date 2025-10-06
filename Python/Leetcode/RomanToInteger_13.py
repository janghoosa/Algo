# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# 로마 숫자를 정수로 변환하는 문제
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToNum(self, s: str) -> int:
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        elif s == 'M':
            return 1000

    def romanToInt(self, s: str) -> int:
        answer = 0
        prev_value = 0
        for char in reversed(s):
            curr_value = self.romanToNum(char)
            if curr_value < prev_value:
                answer -= curr_value
            else:
                answer += curr_value
            prev_value = curr_value
        return answer
