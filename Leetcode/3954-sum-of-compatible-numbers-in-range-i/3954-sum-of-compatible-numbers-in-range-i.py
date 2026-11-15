class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        summ=0
        s=n-k
        e=n+k+1
        for i in range(max(0,n-k),e):
            if abs(n-i)<=k and (n&i)==0:
                summ+=i
        return summ