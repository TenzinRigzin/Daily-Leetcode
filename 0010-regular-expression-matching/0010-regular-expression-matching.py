class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] = does s[:i] match p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* matching empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Option 1: x* matches zero occurrences -> skip "x*"
                    zero_case = dp[i][j - 2]
                    
                    # Option 2: x* matches one more occurrence of current char
                    one_or_more_case = False
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        one_or_more_case = dp[i - 1][j]
                    
                    dp[i][j] = zero_case or one_or_more_case
                else:
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]