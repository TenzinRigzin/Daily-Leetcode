class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        CharSet=set()
        ans=0
        for right in range(len(s)):
            while (s[right] in CharSet):
                CharSet.remove(s[left])
                left+=1
            CharSet.add(s[right])
            ans = max(ans,right-left+1)
        return ans
            