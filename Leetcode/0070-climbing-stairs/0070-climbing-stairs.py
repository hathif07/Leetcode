class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[1]*n
        count=1
        for i in range(int(n/2)):
            del arr[-1]
            #arr[0]=2
            #arr.append(2)
            arr[i]=2
            tn=len(arr)
            n1=arr.count(2)
            n2=arr.count(1)
            num=1
            for a in range(1,tn+1):
                num*=a
                
            d1=1
            d2=1
            for b in range(1,n1+1):
                d1*=b
            for c in range(1,n2+1):
                d2*=c
                
            count += num//(d1*d2)
        return count