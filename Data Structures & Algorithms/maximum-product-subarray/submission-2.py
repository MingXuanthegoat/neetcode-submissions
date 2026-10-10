class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        A = []
        cur = []
        res = float('-inf')


        # Split into subarrays using 0
        for num in nums:
            res = max(res, num)

            if num == 0:
                if cur:
                    A.append(cur)
                
                cur = []
            
            else:
                cur.append(num)
        
        if cur:
            A.append(cur)
        

        # Iterate through the subarrays
        for sub in A:

            negs = sum(1 for i in sub if i < 0)
            prod = 1 # current running product val
            need = negs if negs % 2 == 0 else negs - 1 # how many negatives we need
            negs = 0 # track the number of negs 
            j = 0

            for i in range(len(sub)): # Iterating through that single subarray

                prod *= sub[i] # calculate the prod 

                if sub[i] < 0: # If its negative
                    negs += 1
                    while negs > need: # Too many negatives
                        prod //= sub[j] # dividing out elements to remove them 

                        if sub[j] < 0:
                            negs -= 1
                        
                        j += 1 # move tracker to the latest negative
                
                if j <= i:
                    res = max(res, prod)
        
        return res

        


        