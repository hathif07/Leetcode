class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        r=0
        while columnNumber>0:
            columnNumber-=1
            r=columnNumber%26
            s+=chr(ord('A')+r)
            columnNumber//=26

        return s[::-1]
