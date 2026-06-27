from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = self.makeKey(word)
            anagrams[key].append(word)

        return list(anagrams.values())

    def makeKey(self, string):
        count = [0] * 26
        for char in string:
            count[ord(char) - ord("a")] += 1
        return tuple(count)
