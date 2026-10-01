class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        track = {}

        for i in nums:
            track[i] = 1 + track.get(i, 0)
        
        arr = []

        for n, c in track.items():
            arr.append([c, n])
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
