class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Simple is O(n^2) comp of every l and r set of endpoints

        #I fail to see a way sorting/searching helps, so probably noothing nlogn

        #So what linear passes would help?
       
        #simplest would be l = 0, r =len(nums)
        #or l= 0, r = 1

        #everything is an int - how is this exploitable?
        #should we have sign logic? if we have a negative product, goal


        #if all numbers are positive, full range

        #if only one negative, try to exclude it


        """
        we carry on the biggest positive prod containing r-1 pos_prod
        we carry the greatest magnitude negative prod containing r-1 neg_prod
        we carry max_prod, which may not necessarily include r-1

        If we come accross a positive number in the newly explored r:
            what if the value is 0?
                then both pos_prod, neg prod = 0,0
            what if the value is positive?
                then pos_prod *= nums[r]
                and neg_prod *= nums[r]

            what if it is negative?
                then neg_prod *= nums[r]*pos_prod

                what about pos_prod?
                    it could be nums[r]*neg_prod

        """
        if len(nums) == 1:
            return nums[0]

        max_prod = max( nums[0],nums[1],nums[0]*nums[1] )
        #need to figure out initial condition
        pos_prod = max( 0,nums[1],nums[0]*nums[1])
        neg_prod = min( 0,nums[1],nums[0]*nums[1])


        #what do you do with pos_prod and neg_prod if no such thing exists?, that is, no product of desired sign includes the r-1 index?
        for r in range(2,len(nums)):
            """if nums[r] == 0:
                pos_prod = 0
                neg_prod = 0

            if nums[r] > 0:
                pos_prod *= max( nums[r], nums[r]*pos_prod )
                neg_prod *= min( nums[r], nums[r]*neg_prod )

            if nums[r] < 0:
                neg_prod *= nums[r]*pos_prod
                nums[r]*neg_prod
            """
            #print( "r,nums[r],pos_prod*nums[r],neg_prod*nums[r]", r,nums[r],pos_prod*nums[r],neg_prod*nums[r])

            pos_prod_temp = max( 0,nums[r],pos_prod*nums[r],neg_prod*nums[r])
            neg_prod = min( 0,nums[r],pos_prod*nums[r],neg_prod*nums[r])
            pos_prod = pos_prod_temp
            
            max_prod = max(max_prod,pos_prod)

        return max_prod