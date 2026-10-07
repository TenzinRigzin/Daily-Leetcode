class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        path = []

        def backtrack(open_count: int, close_count: int) -> None:

            if len(path) == 2 * n:
                result.append(''.join(path))
                return


            if open_count < n:
                path.append('(')
                backtrack(open_count + 1, close_count)
                path.pop()  # backtrack

            if close_count < open_count:
                path.append(')')
                backtrack(open_count, close_count + 1)
                path.pop()  # backtrack

        backtrack(0, 0)
        return result