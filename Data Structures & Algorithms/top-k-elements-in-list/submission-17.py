class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        li=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        arr=[]
        for i,j in freq.items():
            arr.append([j,i])
        arr.sort()
        res=[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

                
            
