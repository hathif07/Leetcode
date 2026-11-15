class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        t=s[::-1]
        word=0
        for i in range(len(t)):
            if t[i]!=' ':
                count+=1
                word=1
            elif t[i]==' ':
                if word==0:
                    continue
                else:
                    break

        return count
        #split()
