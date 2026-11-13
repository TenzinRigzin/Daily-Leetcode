from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0                  # operations needed to fix the window nums[i..j]
        dq = deque()              # (adjusted value, count); front = right end, back = left end
        j = n - 1                 # right end of the current window

        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1

            # nums[i] becomes the prefix max for smaller groups to its right
            while dq and dq[-1][0] < num:
                v, c = dq.pop()
                count += c
                cost += (num - v) * c
            dq.append((num, count))

            # Too expensive: drop elements from the right end
            while cost > k:
                v, c = dq.popleft()
                cost -= v - nums[j]       # nums[j] was raised from nums[j] to v
                j -= 1
                if c > 1:
                    dq.appendleft((v, c - 1))

            ans += j - i + 1              # every right end in [i..j] is feasible

        return ans