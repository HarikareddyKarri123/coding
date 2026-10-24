class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_of_year(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days_in_month[:month - 1]) + day

        alice_start = day_of_year(arriveAlice)
        alice_end = day_of_year(leaveAlice)
        bob_start = day_of_year(arriveBob)
        bob_end = day_of_year(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)