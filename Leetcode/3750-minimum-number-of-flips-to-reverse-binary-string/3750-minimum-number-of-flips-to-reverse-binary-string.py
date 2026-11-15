class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)[2:]
        r=b[::-1]
        count = 0
        for i in range(len(b)):
            if b[i]!=r[i]:
                count+=1
        return count
        