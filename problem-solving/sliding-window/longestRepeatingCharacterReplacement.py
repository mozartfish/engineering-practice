from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        start = 0
        maxFrequency = 0
        for end in range(len(s)):
            count[s[end]] += 1
            maxFrequency = max(maxFrequency, count[s[end]])
            while (end - start + 1) - maxFrequency > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result
