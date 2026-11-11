class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int,
                    need1: int, need2: int) -> int:
        m = min(need1, need2)
        M = max(need1, need2)

        only_singles = need1 * cost1 + need2 * cost2
        mixed = m * costBoth + (need1 - m) * cost1 + (need2 - m) * cost2
        only_both = M * costBoth

        return min(only_singles, mixed, only_both)