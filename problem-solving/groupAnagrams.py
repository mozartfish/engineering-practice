from collections import defaultdict
from typing import List


class Solution:
    def makeKey(self, string):
        charCount = [0] * 26
        for c in string:
            charCount[ord(c) - ord("a")] += 1

        return tuple(charCount)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramStore = defaultdict(list)
        for string in strs:
            key = self.makeKey(string)
            anagramStore[key].append(string)

        return list(anagramStore.values())
