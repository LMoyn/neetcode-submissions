class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        history = {}
        for i in range(0,m):
            for j in range(0,n):
                #print("History final: ", history, "at indices: ", i, j)
                if i == 0 or j == 0:
                    history[str([i,j])] = 1
                else:
                    history[str([i,j])] = history[str([i-1,j])] + history[str([i,j-1])]
        #print("History final: ", history )
        return history[str([m-1,n-1])]