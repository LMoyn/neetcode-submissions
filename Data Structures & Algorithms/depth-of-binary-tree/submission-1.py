# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #In the dequeue, store the depth of nodes so we can iterate on it
        if root is None:
            return 0
        depth = 1
        max_depth = depth
        stack = deque()
        stack.append([root,depth])
        while len(stack):
            #print("stack: ",stack)
            pop = stack.pop()
            #print("pop: ", pop)
            current,depth = pop[0], pop[1]
            #if current.left or current.right:
            #    depth = depth+1
            if current.left:
                stack.append([current.left,depth+1])

            if current.right:
                stack.append([current.right,depth+1])

            max_depth = max(max_depth,depth)

        return max_depth