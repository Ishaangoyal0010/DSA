class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mapp={} 
        maxi=0 
        n=len(s)
        r=0
        l=0
        while r<n:
            if s[r] in mapp:
                l=max(l, mapp[s[r]]+1)
            maxi=max(maxi,r-l+1)
            mapp[s[r]]=r
            r+=1
        return maxi


        