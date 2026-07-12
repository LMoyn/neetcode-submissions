class Solution:
    def rob(self, nums: List[int]) -> int:
        

        num_house = len(nums)
        if(num_house <4):
            return max(nums)

        #calc max where we can only rob up to n-2 instead of n-1

        #DP: build up from 0 to n-2
        

        rob0 = nums[0]
        rob1 = nums[1] # corresponds to robbing most recent
        for i in range(num_house-2-1):
            i = i+2
            #print
            #print("i, rob0,rob1: ", i,rob0,rob1)
            rob_new = max(rob1, rob0+nums[i])
            rob0 = max(rob1,rob0)
            rob1 = rob_new

        #print("final: i, rob0,rob1: ", i,rob0,rob1)

        m0 = rob_new

        print("next")
        #calc max where we cannot rob 0 but can up to n-1
        rob0 = nums[1]
        rob1 = nums[2] # corresponds to robbing most recent
        for i in range(num_house-3):
            i = i+3
            #print("i, rob0,rob1: ", i,rob0,rob1)
            rob_new = max(rob1, rob0+nums[i])
            rob0 = max(rob1,rob0)
            rob1 = rob_new

        m1 = rob_new
        #print("final: i, rob0,rob1: ", i,rob0,rob1)
        #print(m0,m1)

        return max(m0, m1)