import heapq

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #sort by first val:
        prerequisites.sort(key = lambda x: x[0])

        #Construct a graph with some kind of node weight (node = course)

            #Indicate how many pre reqs each course has with this weight


            #We can then schedule whatever course(s) have 0 pre reqs first, 
                #then decriment pre req weight for everything a 0 weight course feeds into

        #build the num pre reqs indicator:
        num_prereqs = dict() #perhaps make a heap? - easiest way is to start with array of count/node pairs

        #when you heapify list of tuples, priority is based on first tuple element

        #therefore pre req count is first element, second is node val
        num_prereqs = [0]*numCourses

        prereq_index = 0

        comes_after = dict()

        for i in range(numCourses):
            num_prereqs[i] = [0,i]
            comes_after[i] = set()
            #Also build dict with key as first course, entry as set of all courses requiring it
            while prereq_index < len(prerequisites) and prerequisites[prereq_index][0] == i:
                #comes_after[i] = curr_set
                #comes_after[i] = comes_after[i].add(prerequisites[prereq_index][1])
                comes_after[i].add(prerequisites[prereq_index][1])
                prereq_index+=1

        #print( "pre build: \n ", num_prereqs)
        for prereq in prerequisites:
            num_prereqs[prereq[1]][0] = num_prereqs[prereq[1]][0] + 1 #
            
            #1 #probably need to condition on existence of key

        #print( "pre heap: \n ", num_prereqs)
        #heapify
        heapq.heapify(num_prereqs)

        #print( "Initial heap: \n ", num_prereqs)
        #print(" COmes after: ", comes_after )

        #iterate over values
        while num_prereqs and num_prereqs[0][0] == 0: #condition is peaking if smallest in heap is 0
            #print("doing loop now")
            curr = heapq.heappop(num_prereqs)
            curr_course = curr[1]
            next_courses = comes_after[curr_course]
            #change the in degree of all next courses

            #need to loop over entire num_prereqs
            for i in range(len(num_prereqs)):
                #print( "num_prereqs, i , next courses: ", num_prereqs , i, next_courses)
                if num_prereqs and next_courses and num_prereqs[i][1] in next_courses:
                    num_prereqs[i][0] = num_prereqs[i][0] - 1

            heapq.heapify(num_prereqs)
            #print( "Iter heap: \n ", num_prereqs)
        
        if num_prereqs and len(num_prereqs):
            return False
        
        return True

        