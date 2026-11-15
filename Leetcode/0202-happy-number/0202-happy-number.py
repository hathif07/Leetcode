class Solution:
    def isHappy(self, n: int) -> bool:
        #n=19
        num=n
        while num!=1:
            summ=0
            if(num==1 or num==7):
                #print(True)
                return True
                #break
            elif(num<10):
                #print(False)
                #k=False
                #break
                return False

            n1=str(num)
            for i in range(len(n1)):
                summ+=int(n1[i])**2
            
            num=summ

        #if(not k):
            #print(True)
        return True