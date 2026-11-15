class Solution:
    def canWinNim(self, n: int) -> bool:
        if n==1 or n==2:
            return True
        elif n%4!=0:
            return True
        else:
            return False