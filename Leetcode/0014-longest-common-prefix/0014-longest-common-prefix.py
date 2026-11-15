class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i >= len(j) or j[i] != strs[0][i]:
                    return s
            s += strs[0][i]
        return s

        
        """s=strs[0]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if s[0]==strs[i][j]:
                    s+=strs[i][j]
                else:
                    #s-=strs[i][j]
                    temp=s.replace(strs[i][j],"")
        return temp;"""            