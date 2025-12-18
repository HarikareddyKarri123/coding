class Solution:
    def sortIt(self, arr):
        odds = []
        evens = []

        for x in arr:
            if x % 2 == 1:
                odds.append(x)
            else:
                evens.append(x)

        odds.sort(reverse=True)
        evens.sort()

        idx = 0
        for x in odds:
            arr[idx] = x
            idx += 1
        for x in evens:
            arr[idx] = x
            idx += 1


