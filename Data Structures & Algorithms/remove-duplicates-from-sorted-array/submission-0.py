class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        record = {}
        dup_count = 0
        Init_size = len(nums)
        while index + dup_count < Init_size:
            num = nums[index]
            #print("num, index, dup_count, nums", num, index, dup_count,nums)
        #for num in nums:
            if str(num) in record:
                dup_count +=1
                nums.pop(index)
            else:
                record[str(num)] = 1    
                index+=1

        return Init_size - dup_count