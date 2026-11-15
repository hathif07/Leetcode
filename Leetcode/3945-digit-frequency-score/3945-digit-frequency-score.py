class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        l=list(s)
        summ,i=0,0
        while l!=[]:
            d=l[0]
            c=l.count(d)
            summ+=(int(d)*c)
            while d in l:
                l.remove(d)

        return summ
