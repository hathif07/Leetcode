class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        t=nums[0]
        l=[]
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]+1:
                if t==nums[i]:
                    l.append(str(t))
                else:
                    l.append(f"{t}->{nums[i]}")
                t=nums[i+1]

        if t==nums[-1]:
            l.append(str(t))
        else:
            l.append(f"{t}->{nums[-1]}")

        return l
