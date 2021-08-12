# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = head
        cur = head
        first = True
        while cur:
            if first:
                first = False
                cur = cur.next
                if head.val==val:
                    head = head.next
                    first = True
                    prev = head
                    cur = head
            else:
                deleted = False
                if cur.val==val:
                    deleted = True
                    #Delete this element
                    prev.next = cur.next
                cur = cur.next
                if not deleted:
                    prev=prev.next
        return head
                
            
            