# In Subsequence
# https://leetcode.com/problems/is-subsequence/
# 투포인터 문제
# 두 문자열을 순회하면서 s의 모든 문자가 t에 순서대로 포함되는지 확인하는 문제
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in t:
            if i >= len(s):
                return True
            if j == s[i]:
                i += 1
        return i == len(s)