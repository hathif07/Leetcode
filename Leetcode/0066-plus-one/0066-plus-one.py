class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        max=len(digits)
        sum=0
        for i in range(len(digits)):
            sum+=(digits[i]*(10**(max-1-i)))

        sum+=1

        res=[]
        temp=str(sum)
        for i in temp:
            res.append(int(i))

        return res


