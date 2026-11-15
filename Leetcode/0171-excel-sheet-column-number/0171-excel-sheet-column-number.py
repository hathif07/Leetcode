class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n=0
        for i in columnTitle:
            n=n*26+(ord(i)-ord('A')+1)
        return n