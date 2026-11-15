class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        s1=[]
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                l.append(s[i])

        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                x=l.pop()
                s1.append(x)
            else:
                s1.append(s[i])
                
        s="".join(s1)

        return s

        