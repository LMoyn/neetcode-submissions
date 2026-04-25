from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Approach:
        Make sets of visited?
        queue of non visited to avoid backtracking?
            No, because we could navigate down in a search in a way that would look like backtracking?

        Pop non visited set until we get a node with value one

        Just decide on search: DFS
            Stack
            dequeue
                append
                pop
        '''

        length = len(grid)
        width = len(grid[0])
        count = 0
        #fill not visited
        non_visit = set()
        for l in range(length):
            for w in range(width):
                coords = str([l,w])
                #print("coords: ", coords)
                non_visit.add( (l,w))
        while len(non_visit):
            current = non_visit.pop()
            #print( "current: ", current)
            c1 = current[0]
            c2 = current[1]
            #print( "grid val: ", grid[i][j] )
            if grid[c1][c2] == '1': #found start of valid island
                count+=1
                #Start doing search.
                #print("Found start!")
                #print( "grid val: ", grid[c1][c1] )
                #print( "location: ", current)


                #Check L,R,U,D
                    #Create a list of tuples, then loop

                #If visited
                    #Ignore
                #If not visited:
                    #If 0
                        #Remove from non_visit
                    #If 1
                        #Remove from non_visit
                        #Add item to deque
                Stack = deque()
                Stack.append(current)
                while len(Stack):
                    island_coords = Stack.pop()
                    i = island_coords[0]
                    j = island_coords[1]
                    L = (i-1,j)
                    R = (i+1,j)
                    U = (i,j-1)
                    D = (i,j+1)
                    for move in [L,R,U,D]:
                        if move in non_visit:
                            non_visit.remove(move)
                            if grid[move[0]][move[1]] == '1':
                                Stack.append(move)
                                #print(" Added to stack: ", move)
        return count



                

