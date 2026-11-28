class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)


        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1

        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            multiples[f] = sum(cnt[f::f])

        m = min(p for _, p in items)          
        R = budget
        ans = 0

        for f, p in sorted(items, key=lambda x: x[1]):
            if p >= 2 * m:                   
                break
            g = multiples[f] - 1       
            if g == 0:
                continue
            q = min(g, R // p)                 
            R -= q * p
            ans += 2 * q                       
            if q < g:                          
                break

        return ans + R // m                    