class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l) // 2

            # Check if its part of left sorted portion
            if nums[m] < nums[r]:
                r = m

            # Check if its part of right sorted portion
            else:
                l = m + 1
            
        return nums[l]





        

        