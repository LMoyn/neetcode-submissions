class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Brute force: O(n^3) comparison of every set of 3 triplets


        Found = [False]*3
        for i in range(3):
            for triplet in triplets:
                if target[i] == triplet[i] and target[(i+1)%3] >= triplet[(i+1)%3] and target[(i+2)%3] >= triplet[(i+2)%3]:
                    Found[i] = True
                    break
        return Found[0] and Found[1] and Found[2]
        

        """
        candidates = [0]*3
        for i in range(3):
            curr_set = set() #keep overwriting I think
            for triplet in triplets:
                #print( "iter, I indices, I+1%3 indices, i+2%3 indices: ", i, target[i],triplet[i],target[(i+1)%3], triplet[(i+1)%3],target[(i+2)%3],triplet[(i+2)%3])
                if target[i] == triplet[i] and target[(i+1)%3] >= triplet[(i+1)%3] and target[(i+2)%3] >= triplet[(i+2)%3]:
                    curr_set.add(tuple(triplet))
            candidates[i] = curr_set


        print( "candidates: ", candidates )
        #Loop over all combos - is this even needed? if all sets are nonempty then don't we win
        if len(candidates[0]) and len(candidates[1]) and len(candidates[2]):
            return True

        #Since all we need is existence, storage doesn't matter. We can just make indicators of if we found anything

        return False

        """


        """for x_cand in candidates[0]:
            for y_cand in candidates[1]:
                for z_cand in candidates[2]:
                    if

        smoother brute force ish:

        get list of all triplets with correct x, correct y, correct z

        correct x:
            x value matches
            y is less than or equal to desired y
            z is as well
        By symmetry something similar for x and y correct

        compare those to see what works


        can build so the comparisons are more efficient/logical?

        """


        """
        probably something better


        """


        

        