# Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# 두 문자열이 아나그램인지 확인하는 문제
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = Counter(s)
        tt = Counter(t)
        if ss == tt:
            return True
        else:
            return False
        