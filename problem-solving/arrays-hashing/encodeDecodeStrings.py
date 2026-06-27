from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        # 1. find the length of the string
        # 2. stop when we see #
        # 3. move character by character based on the string length to get the entire string
        # 4. add the string to the list
        # 5. repeat same process

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            s_len = int(s[i:j])
            i = j + 1
            j = i + s_len
            result.append(s[i:j])
            i = j
        return result
