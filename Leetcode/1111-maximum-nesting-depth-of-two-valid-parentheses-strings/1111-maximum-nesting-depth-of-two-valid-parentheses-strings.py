class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n=len(seq)
        l=[0]*n
        d=0
        for i in range(len(seq)):
            if seq[i]=='(':
                d+=1
                l[i]=d%2
            else:
                l[i]=d%2
                d-=1
            
        return l
