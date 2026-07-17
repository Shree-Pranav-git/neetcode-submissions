class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l=0
        r=0
        while l<(m+n) and r<n:
            if nums1[l]==0:
                nums1[l]=nums2[r]
                r+=1
            l+=1
        return nums1.sort()



        """
        Do not return anything, modify nums1 in-place instead.
        """
        