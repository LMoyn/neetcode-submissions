class Solution:
    def rob(self, nums: List[int]) -> int:
        

        num_house = len(nums)
        if(num_house <4):
            return max(nums)

        #calc max where we can only rob up to n-2 instead of n-1

        #DP: build up from 0 to n-2
        

        rob0 = nums[0]
        rob1 = nums[1] # corresponds to robbing most recent
        for i in range(2,num_house-1):
            rob_new = max(rob1, rob0+nums[i])
            rob0 = max(rob1,rob0)
            rob1 = rob_new

        m0 = rob_new

        #calc max where we cannot rob 0 but can up to n-1
        rob0 = nums[1]
        rob1 = nums[2] # corresponds to robbing most recent
        for i in range(3,num_house):
            rob_new = max(rob1, rob0+nums[i])
            rob0 = max(rob1,rob0)
            rob1 = rob_new

        m1 = rob_new

        return max(m0, m1)