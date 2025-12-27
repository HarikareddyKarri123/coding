import heapq

class Solution:
    def mostBooked(self, n: int, meetings):
        # Sort meetings by start time
        meetings.sort()

        # Min-heap of available rooms
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        # Min-heap of ongoing meetings: (end_time, room)
        busy_rooms = []

        # Count meetings per room
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that have finished before current meeting starts
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                # Delay meeting
                finish, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (finish + duration, room))

            count[room] += 1

        # Return room with max meetings (smallest index if tie)
        return count.index(max(count))
