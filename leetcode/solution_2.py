class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # only append() or pop()
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif len(stack) == 0 or bracket != brackets[stack.pop()]:
                return False

        return len(stack) == 0
