class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')


        divs = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            divs[L] = [d for d in range(1, L) if L % d == 0]


        cost = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i + 2, n + 1):
                L = j - i
                best = INF
                for d in divs[L]:
                    c = 0
                    for r in range(d):         
                        lo = i + r                
                        hi = j - d + r             
                        while lo < hi:            
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                        if c >= best:             
                            break
                    best = min(best, c)
                    if best == 0:
                        break
                cost[i][j] = best

        f = [[INF] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):           
                for h in range(2 * (j - 1), i - 1):
                    if f[h][j - 1] < INF:
                        v = f[h][j - 1] + cost[h][i]
                        if v < f[i][j]:
                            f[i][j] = v
        return f[n][k]