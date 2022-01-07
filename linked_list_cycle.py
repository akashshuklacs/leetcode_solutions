# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head == None:
            return False
        while fast.next!=None and fast.next.next!=None:
            fast= fast.next.next
            slow= slow.next
            if fast == slow:
                return True
        return False
