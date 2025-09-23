# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# 두 문자열이 서로 1:1 매핑이 되는지 확인하는 문제
# 
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}

        for sc, tc in zip(s, t):
            if sc in s_to_t:
                if s_to_t[sc] != tc:
                    return False
            else:
                s_to_t[sc] = tc
            
            if tc in t_to_s:
                if t_to_s[tc] != sc:
                    return False
            else:
                t_to_s[tc] = sc
        
        return True
    
# Counter를 이용한 풀이 - 실패
# Time Complexity: O(n)
# Space Complexity: O(n)
# Input = "bbbaaaba"
# Output = "aaabbbba" (실패)

from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = Counter(s)
        tt = Counter(t)
        print(ss.values(), tt.values())
        if list(ss.values()) == list(tt.values()):
            return True
        else:
            return False
        