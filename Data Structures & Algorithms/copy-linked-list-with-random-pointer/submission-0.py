# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         dummy = Node(0)
#         curr = head
#         created = {}
#         while curr:
#             next_new = None
#             random_new = None
#             if curr.next:
#                 if curr.next not in created:
#                     next_new = Node(curr.next.val)
#                     created[curr.next] = next_new
#                 else:
#                     next_new = created[curr.next]
#             if curr.random:
#                 random_new = Node(curr.random.val)
#             new = Node(curr.val, next_new, random_new)
#             if not dummy.next:
#                 dummy.next = new
#             curr = curr.next
#         return dummy.next
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Map original nodes to their copies
        old_to_new = {}
        
        # First pass: Create all nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # Second pass: Set next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]