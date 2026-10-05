class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        tracker = set()

        ret = 0
        l = 0 

        for r in range(len(s)):
               
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1

            tracker.add(s[r])
            ret = max(ret, r - l + 1)
        
        return ret


            


        
        