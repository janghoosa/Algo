# Ransom Note
# https://leetcode.com/problems/ransom-note/
# Counter를 이용한 풀이
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
    

# 딕셔너리를 이용한 풀이
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = defaultdict(int)
        magc = defaultdict(int)
        for note in ransomNote:
            ransom[note] += 1
        for note in magazine:
            magc[note] += 1
        for note in ransom.keys():
            if magc[note] < ransom[note]:
                return False
        return True