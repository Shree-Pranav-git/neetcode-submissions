class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1=nums
        nums2=nums
        nums2.extend(nums1)
        return nums2