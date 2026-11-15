class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        for j in range(len(nums)):
            if target<nums[j]:
                return j
        return len(nums)
