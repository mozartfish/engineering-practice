from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tCount = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            tCount[c] += 1

        have = 0
        need = len(tCount)
        result = [-1, -1]
        resultLen = float("infinity")

        start = 0
        for end in range(len(s)):
            c = s[end]
            window[c] += 1

            if c in tCount and window[c] == tCount[c]:
                have += 1

            while have == need:
                if (end - start + 1) < resultLen:
                    result = [start, end]
                    resultLen = end - start + 1

                window[s[start]] -= 1
                if s[start] in tCount and window[s[start]] < tCount[s[start]]:
                    have -= 1
                start += 1

        start, end = result

        if resultLen != float("infinity"):
            return s[start : end + 1]

        return ""
