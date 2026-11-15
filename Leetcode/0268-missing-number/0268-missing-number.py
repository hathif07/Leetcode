class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count=len(nums)
        for i in range(count+1):
            if i not in nums:
                return i
