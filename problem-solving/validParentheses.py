class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parensStore = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in parensStore:
                if stack and (stack[-1] == parensStore[c]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True

        return False
