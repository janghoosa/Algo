# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# 알파벳과 숫자만 남기고 모두 제거한 후 팰린드롬인지 확인하는 문제
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ''.join([c for c in s.lower().replace(" ", "") if c.isalnum()])
        return sentence == sentence[::-1]