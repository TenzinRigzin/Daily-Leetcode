class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:  
                top = stack.pop() if stack else '#'
                if top != pairs[ch]:
                    return False
            else:  
                stack.append(ch)

        return not stack