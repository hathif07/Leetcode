class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()
        """for i in range(len(nums1)):
            mi=nums1[0]
            for j in range(i,len(nums1)):
                if nums1[j]<mi:
                    mi=nums1[j]
            nums1[i]=mi
               """     