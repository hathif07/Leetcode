class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ta=int(a,2)
        tb=int(b,2)
        return bin(ta+tb)[2:]