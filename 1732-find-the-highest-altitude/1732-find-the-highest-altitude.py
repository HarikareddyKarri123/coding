class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        att=0
        hig=0
        for g in gain:
            att+=g
            hig=max(hig,att)
        return hig
        