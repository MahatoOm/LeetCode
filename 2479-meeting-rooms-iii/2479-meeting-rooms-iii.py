import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n  # count of how many times each room is booked
        busy = []        # heap to track rooms currently in use: (end_time, room_index)
        free_rooms = list(range(n))  # heap to track available room indices
        heapq.heapify(free_rooms)

        meetings.sort(key=lambda x: x[0])  # sort meetings by start time

        for start, end in meetings:
            # Free up rooms that have become available before this meeting starts
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # Assign to the smallest-indexed available room
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy, (end, room))
                rooms[room] += 1
            else:
                # Wait for the room that becomes free the earliest
                earliest_end, room = heapq.heappop(busy)
                duration = end - start
                new_end = earliest_end + duration
                heapq.heappush(busy, (new_end, room))
                rooms[room] += 1

        # Find the room with the maximum number of meetings
        max_meetings = max(rooms)
        for i, count in enumerate(rooms):
            if count == max_meetings:
                return i
