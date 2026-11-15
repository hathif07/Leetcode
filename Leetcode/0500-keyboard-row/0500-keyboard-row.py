class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first="qwertyuiop"
        second="asdfghjkl"
        third="zxcvbnm"
        l=[]
        s=""
        for i in range(len(words)):
            if words[i][0].lower() in first:
                s=first
            elif words[i][0].lower() in second:
                s=second
            else:
                s=third
            t=True
            for j in range(len(words[i])):
                if words[i][j].lower() not in s:
                    t=False
                    break
            if t:
                l.append(words[i])

        return l