# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        current = root
        carry = 0
        
        while True:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            total = val1 + val2 + carry
            if total >= 10:
                total -= 10
                carry = 1
            else:
                carry = 0
            current.val = total

            if l1 is None and l2 is None and carry == 0:
                break
            else:
                current.next = ListNode()
                current = current.next
        return root
