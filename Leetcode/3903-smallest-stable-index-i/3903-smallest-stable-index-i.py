class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            ma = max(nums[0:i+1])
            mi = min(nums[i:n])

            if ma - mi <= k:
                return i

        return -1
