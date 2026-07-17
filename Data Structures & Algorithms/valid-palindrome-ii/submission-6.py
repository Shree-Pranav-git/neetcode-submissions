class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skippedL= s[l+1:r+1]
                skippedR=s[l:r]
                return skippedL == skippedL[::-1] or skippedR==skippedR[::-1]
            l,r=l+1,r-1
        return True

        