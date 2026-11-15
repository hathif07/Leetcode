class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            lin=[1]*(i+1)
            for j in range(1,i):
                lin[j]=l[i-1][j-1]+l[i-1][j]

            l.append(lin)
        return l
                
