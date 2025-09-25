from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by end time
        events.sort(key=lambda x: x[1])
        
        # Step 2: Track the maximum value of a single event so far
        max_result = 0
        max_single_event = 0
        
        # Lists to store end times and corresponding maximum values
        end_times = []
        max_values = []
        
        for start, end, value in events:
            # Step 3: Find the latest non-overlapping event using binary search
            idx = bisect_right(end_times, start - 1) - 1
            
            # If there is a non-overlapping event, combine its value with the current event's value
            if idx >= 0:
                max_result = max(max_result, max_values[idx] + value)
            
            # Update the running maximum for a single event
            max_single_event = max(max_single_event, value)
            
            # Update the result to include just the single event case
            max_result = max(max_result, max_single_event)
            
            # Step 4: Update end_times and max_values
            end_times.append(end)
            max_values.append(max_single_event)
        
        return max_result
