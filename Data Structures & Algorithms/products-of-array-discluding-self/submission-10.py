class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1=[]
        sum=1
        for i in range(len(nums)):
            sum=1
            for j in range(len(nums)):
                if i!=j:
                    sum=sum*nums[j]
            nums1.append(sum)
        return nums1