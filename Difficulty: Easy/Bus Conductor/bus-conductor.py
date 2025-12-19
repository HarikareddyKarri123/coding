class Solution:
    def findMoves(self, chairs, passengers):
        # Sort both lists
        chairs.sort()
        passengers.sort()

        # Calculate total moves
        moves = 0
        for c, p in zip(chairs, passengers):
            moves += abs(c - p)

        return moves

