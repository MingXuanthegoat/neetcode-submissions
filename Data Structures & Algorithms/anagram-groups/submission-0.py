class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tracker = {}

        for i in strs:
            sort = "".join(sorted(i))

            if sort in tracker:
                tracker[sort].append(i)
            else:
                tracker[sort] = [i]
            
        return list(tracker.values())


        