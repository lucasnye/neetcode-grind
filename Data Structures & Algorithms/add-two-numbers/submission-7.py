# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         curr1, curr2 = l1, l2
#         carry = 0
#         while curr1 and curr2:
#             curr1.val += curr2.val #18
#             if curr1.val // 10 == 1: #true
#                 carry = 1
#                 ones_place = curr1.val % 10
#                 curr1.val = ones_place #8
#                 if curr1.next: #and curr1.next.val >= 9: #true
#                     curr1.next.val += carry
#                 else:
#                     new_node = ListNode(carry)
#                     curr1.next = new_node
#                     return l1
#             curr1 = curr1.next
#             curr2 = curr2.next
#         while curr1:
#             if curr1.val // 10 == 1: #true
#                 carry = 1
#                 ones_place = curr1.val % 10
#                 curr1.val = ones_place #8
#                 if curr1.next: #and curr1.next.val >= 9: #true
#                     curr1.next.val += carry
#                 else:
#                     new_node = ListNode(carry)
#                     curr1.next = new_node
#                     return l1
#             curr1 = curr1.next
#         while curr2:
#             if curr2.val // 10 == 1: #true
#                 carry = 1
#                 ones_place = curr2.val % 10
#                 curr2.val = ones_place #8
#                 if curr2.next: #and curr1.next.val >= 9: #true
#                     curr2.next.val += carry
#                 else:
#                     new_node = ListNode(carry)
#                     curr2.next = new_node
#                     return l1
#             curr2 = curr2.next
#         return l1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10
            new = ListNode(digit)
            curr.next = new
            curr = new
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next