class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        ret_interval = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            #need to keep a start and end for last interval used
            if interval[0] > end:
                ret_interval.append([start,end])
                start = interval[0]
            
            end = max(interval[1],end)

        ret_interval.append([start,end])

        return ret_interval
