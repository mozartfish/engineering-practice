from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        charMap = defaultdict(int)

        for end in range(len(s)):
            if s[end] in charMap:
                start = max(charMap[s[end]] + 1, start)
            charMap[s[end]] = end
            maxLength = max(maxLength, end - start + 1)
        return maxLength
