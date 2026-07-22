class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for l in range(len(heights)):
            r = len(heights)-1
            while l<r:
                mul = (r-l)*min(heights[l],heights[r])
                if mul>=max:
                    max = mul
                r-=1
            
        return max
        