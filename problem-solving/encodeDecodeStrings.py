from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(str(len(string)))
            result.append("#")
            result.append(string)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        # 1. find the length of string
        # 2. stop when we see #
        # 3. move character by character based on string length
        # to get entire string
        # 4. add string to the list

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            string_len = int(s[i:j])
            i = j + 1
            j = i + string_len
            result.append(s[i:j])
            i = j

        return result
