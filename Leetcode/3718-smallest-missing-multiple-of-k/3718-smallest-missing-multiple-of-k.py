class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j=k
        for i in range(len(nums)+1):
            if j%k==0 and (j not in nums):
                return j
            j+=k