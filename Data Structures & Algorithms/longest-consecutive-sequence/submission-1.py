class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = {}
        for num in nums:
            num_map[str(num)] = num
        #start with a key
        max_count = 0
        #See how far up a sequence you can go
        for num in nums:
            count = 0
            neg_count = -1
            current_num = num
            #print(str(current_num))
            #print("str(current_num) in num_map:", str(current_num) in num_map)
            #Expand in positive direction
            while str(current_num) in num_map:
                num_map.pop(str(current_num))
                count+=1
                current_num+=1
                print("Loop count: ", count)
            #Expand in negative direction
            neg_count = 0
            current_num = num-1
            while str(current_num) in num_map:
                num_map.pop(str(current_num))
                neg_count+=1
                current_num-=1
                #print("Loop count: ", count)
            count+= neg_count
            if max_count < count:
                #print("initial max_count", max_count)
                max_count = count


        return max_count
