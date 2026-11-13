from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0            
        dq = deque()           
        j = n - 1     

        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1

 
            while dq and dq[-1][0] < num:
                v, c = dq.pop()
                count += c
                cost += (num - v) * c
            dq.append((num, count))

            while cost > k:
                v, c = dq.popleft()
                cost -= v - nums[j]      
                j -= 1
                if c > 1:
                    dq.appendleft((v, c - 1))

            ans += j - i + 1          

        return ans