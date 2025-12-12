class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second = -1

        for x in arr:
            if x > largest:
                second = largest
                largest = x
            elif x > second and x != largest:
                second = x

        return second
