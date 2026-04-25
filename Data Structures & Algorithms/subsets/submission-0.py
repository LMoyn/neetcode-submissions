import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets_copy = copy.deepcopy(subsets)
            for subset in subsets_copy: #doesn't matter, still pointing to subset I think
                print("subset: ", subset)
                new_subset = subset+ [num]
                print("new_subset: ", new_subset)
                subsets.append(new_subset)
            #copy every item in subsets 
        return subsets