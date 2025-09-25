# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# 정렬 후 첫번째 문자열과 마지막 문자열을 비교하면서 접두사를 찾는 문제
# Time Complexity: O(n log n) (정렬 시간)
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]