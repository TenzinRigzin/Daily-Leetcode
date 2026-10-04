class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:  # it's a closing bracket
                # Pop top if stack non-empty, else use a sentinel that matches nothing
                top = stack.pop() if stack else '#'
                if top != pairs[ch]:
                    return False
            else:  # it's an opening bracket
                stack.append(ch)

        return not stack  # valid only if every opener was matched (stack empty)