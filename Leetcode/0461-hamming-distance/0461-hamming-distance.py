class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=x^y
        s=bin(n)
        return s.count('1')