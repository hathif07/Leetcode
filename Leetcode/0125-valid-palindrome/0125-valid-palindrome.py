class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in range(len(s)):
            if s[i].isalnum():
                if s[i].isupper():
                    st+=s[i].lower()
                else:
                    st+=s[i]
                '''elif s[i].isnumeric():
                    st+=s[i]'''
        
        t=st[::-1]

        if t==st:
            return True
        else:
            return False
            