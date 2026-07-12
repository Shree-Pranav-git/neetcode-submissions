class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        n=n//2
        d=dict()
        for el in nums:
            if el in d:
                d[el]+=1
            else:
                d[el]=1
        for i in d:
            if d[i]>n:
                return i
            