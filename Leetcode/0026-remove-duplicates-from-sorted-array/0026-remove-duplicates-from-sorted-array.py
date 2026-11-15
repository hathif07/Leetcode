class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        j=0
        #x=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
                
        return j+1