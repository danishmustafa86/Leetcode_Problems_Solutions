class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]
        for start , end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                lastEnd = max(lastEnd, end)
                output[-1][1] = lastEnd
            else:
                output.append([start,end])
        return output
