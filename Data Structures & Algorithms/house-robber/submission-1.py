class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return max( nums[0], nums[1])
        if len(nums) == 1:
            return nums[0]
        dont_rob = nums[0] #didnt rob last house
        rob_last = nums[1] #did rob last hous
        index = 3


        for index in range(2,len(nums)):
            rob_reward = dont_rob + nums[index]
            dont_rob = max( dont_rob, rob_last)
            rob_last = rob_reward
            print("index, dont_rob, rob_last", index, dont_rob, rob_last)


        return max( dont_rob, rob_last)