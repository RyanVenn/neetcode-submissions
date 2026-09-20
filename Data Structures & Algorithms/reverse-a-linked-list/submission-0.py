# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            ne = head.next
            head.next = prev
            prev = head
            head = ne

        
        return prev

        

# head steps through, we need a prev
# next = head.next
# next = head.next 