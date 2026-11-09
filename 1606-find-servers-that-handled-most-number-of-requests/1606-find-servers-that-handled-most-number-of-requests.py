import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))     
        heapq.heapify(free)
        busy = []             
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):

            while busy and busy[0][0] <= start:
                _, s = heapq.heappop(busy)

                heapq.heappush(free, i + (s - i) % k)


            while free and free[0] < i:
                v = heapq.heappop(free)
                heapq.heappush(free, v + ((i - v + k - 1) // k) * k)


            if not free:
                continue

            v = heapq.heappop(free)  
            s = v % k
            count[s] += 1
            heapq.heappush(busy, (start + dur, s))

        best = max(count)
        return [s for s, c in enumerate(count) if c == best]