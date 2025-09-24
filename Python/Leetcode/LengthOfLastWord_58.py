# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# 문자열을 뒤에서부터 탐색하면서 마지막 단어의 길이를 구하는 문제
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        check = False
        answer = 0
        for idx in range(len(s)-1, -1, -1):
            if check:
                if s[idx] == ' ':
                    return answer
                else:
                    answer += 1
            else:
                if s[idx] != ' ':
                    check = True
                    answer += 1
        return answer