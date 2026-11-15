class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        t=""
        for i in range(len(s)):
            t=s[1:]+s[:1]
            if t==goal:
                return True
            s=t

        return False