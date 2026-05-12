# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        curr = head
        index = 0
        while curr:
            if not seen:
                seen[curr] = index
                index += 1
                curr = curr.next
                continue
            if curr in seen:
                print(seen[curr])
                return True
            seen[curr] = index
            index += 1
            curr = curr.next
        return False