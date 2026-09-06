class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []
        path = []  # current combination being built

        def backtrack(index: int) -> None:
            # Base case: path is as long as digits -> complete combination
            if index == len(digits):
                result.append(''.join(path))
                return

            letters = phone[digits[index]]
            for ch in letters:
                path.append(ch)          # choose
                backtrack(index + 1)     # explore
                path.pop()                # un-choose (backtrack)

        backtrack(0)
        return result