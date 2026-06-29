class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 1

        def expand(l: int, r: int) -> None:
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # After loop: s[l+1 : r] is the palindrome
            length = r - l - 1
            if length > max_len:
                max_len = length
                start = l + 1

        for i in range(len(s)):
            expand(i, i)      # odd-length palindrome
            expand(i, i + 1)  # even-length palindrome

        return s[start : start + max_len]