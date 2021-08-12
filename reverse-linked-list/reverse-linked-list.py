# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev:
            if prev.next:
                cur = prev.next
                if cur and cur.next:
                    nextt = cur.next
                else:
                    nextt = None
            else:
                return prev
        else:
            return None
        first = True
        while cur:
            #Case for the last element
            if first:
                first = False
                head.next = None
            if not nextt:
                cur.next = prev
                head = cur
                break
            else:
                #reverse the pointers
                cur.next = prev
                #Reset the pointers
                prev = cur
                cur = nextt
                nextt = cur.next
        return head
                