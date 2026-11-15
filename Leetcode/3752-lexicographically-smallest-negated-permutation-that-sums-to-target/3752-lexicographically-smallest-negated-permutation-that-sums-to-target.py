class Solution(object):
    def lexSmallestNegatedPerm(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: List[int]
        """
        if target < -(n*(n+1)//2) or target>(n*(n+1)//2):
            return []
            
        total=n*(n+1)//2
        d=total-target
        
        if d%2!=0:
            return []
        x=d//2
        result=set()

        for i in range(n,0,-1):
            if x>=i:
                x-=i
                result.add(i)

        arr=[]
        for i in range(1,n+1):
            if i in result:
                arr.append(-i)
            else:
                arr.append(i)

        arr.sort()


        return arr