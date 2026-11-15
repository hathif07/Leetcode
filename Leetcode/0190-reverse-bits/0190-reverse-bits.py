class Solution:
    def reverseBits(self, n: int) -> int:
        nbs=bin(n)[2:].zfill(32)
        nbstemp=nbs[::-1]
        nb=int(nbs,2)
        nbint=int(nbstemp,2)
        return nbint

