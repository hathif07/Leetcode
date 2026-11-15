class Solution(object):
    def countValidPrefixes(self, s):
        
        """
        :type s: str
        :rtype: int
        """
        z=0
        o=0
        c=0
        for i in range(len(s)):
            if s[i]=='0':
                z+=1
            else:
                o+=1

            if(abs(z-o)<=1):
                c+=1
        return c
        
        











        