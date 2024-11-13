from typing import *

class Solution:
    """
    Approaches:
    - Greedy algorithm: Sort start time and end times, and sweep from 0 increasingly,
        if we meet a start time we just add one to the room number, and if we meet a end
        time, we just delete one from the room number. During the process just keep track
        of the maxium.

        This works because we don't need to track exactly which room is checked in or 
        checked out, we just need to know how many meetings are concurrently happening.
        we don't care about the room scheduling that which meeting room that following 
        meeting should go.

        Time Complexity: O(Nlog(N))
        Space Complexity: O(N)

    - Min Heap: Similar to above, but just different ways of getting the smallest value
        of start and end time.
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Assume inputs are valid and validation logic will be skipped here
        MAX_TIME = 10 ** 6 + 1
        start_times: List[int] = []
        end_times: List[int] = []

        for start_time, end_time in intervals:
            start_times.append(start_time)
            end_times.append(end_time)

        start_times.sort()
        end_times.sort()

        start_index = 0
        end_index = 0
        current_num_room = 0
        max_num_room = 0
        list_size = len(intervals)
        while start_index < list_size and end_index < list_size:
            next_start_time = start_times[start_index] if start_index < list_size else MAX_TIME
            next_end_time = end_times[end_index]
            if next_start_time < next_end_time:
                current_num_room += 1
                start_index += 1
            else: # if next_start_time == next_end_time we check out the room first to avoid open an extra room
                current_num_room -= 1
                end_index += 1
            max_num_room = max(current_num_room, max_num_room)
            
        return max_num_room

