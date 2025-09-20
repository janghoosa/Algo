# Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# 문자열 내에서 특정 문자열이 처음으로 나타나는 위치를 찾는 문제
# Time Complexity: O(n * m) (n: haystack 길이, m: needle 길이)
# Python의 내장 함수 사용 (C로 구현되어 있어 매우 빠름!!)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)