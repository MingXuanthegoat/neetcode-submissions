class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) > 1:
            d = [0] * len(nums)

            for i in range(len(nums)):
                d[i] = max(d[i - 1], nums[i] + d[i-2])

            return d[len(nums) - 1]
        else:
            return nums[0]
