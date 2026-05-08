class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                continue
            else:
                flag=1
        if flag==1:
            return True
        else:
            return False