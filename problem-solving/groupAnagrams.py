from collections import defaultdict
from typing import List


class Solution:
    def makeKey(self, s):
        charCount = [0] * 26
        for c in s:
            charCount[ord(c) - ord("a")] += 1
        return tuple(charCount)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            key = self.makeKey(string)
            result[key].append(string)

        return list(result.values())
