import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # sort engineers by efficiency, descending
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        min_heap = []   # min-heap of speeds, capped at size k
        speed_sum = 0
        best = 0
        
        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            speed_sum += spd
            
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            
            # eff is guaranteed to be the min efficiency of the current pool
            best = max(best, speed_sum * eff)
        
        return best % MOD