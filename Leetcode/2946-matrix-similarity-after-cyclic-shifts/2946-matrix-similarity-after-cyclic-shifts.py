class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m=len(mat)
        n=len(mat[0])
        s=[[]]
        for i in range(m):
            k2=k%n
            if i%2==0:
                s=mat[i][k2:]+mat[i][:k2]
            else:
                s=mat[i][-k2:]+mat[i][:-k2]
            if s!=mat[i]:
                return False
        """if s==mat[0]:
            return True
        else:
            return False"""
        return True
        
