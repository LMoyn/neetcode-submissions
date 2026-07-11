# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #simple solution: maintain set visited and return true if found something in it
        #if linked list ends before, return false


        visited = set()
        curr = head

        if curr is None:
            return False

        while curr.next: # need to handle edge cases
            node = curr.next
            if node.val in visited:
                return True
            visited.add(node.val)
            curr = node

        return False