class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])  # sort by end time
        
        count = 0          # number of intervals to remove
        prev_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prev_end:       # overlap
                count += 1              # remove this one
            else:
                prev_end = end          # keep this one, update boundary
        
        return count