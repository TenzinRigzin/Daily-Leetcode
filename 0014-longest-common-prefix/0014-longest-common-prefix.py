class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        first = strs[0]

        for i, char in enumerate(first):
            for other in strs[1:]:
                if i >= len(other) or other[i] != char:
                    return first[:i]

        return first