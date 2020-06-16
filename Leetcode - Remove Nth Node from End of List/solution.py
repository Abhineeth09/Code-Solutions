# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size=0
        if head:
            size=1
        pointer=head
        pointer2=head
        while pointer:
            pointer=pointer.next
            size+=1
            if size==n+1:
                pointer2=head
            if size>n+1:
                pointer2=pointer2.next
            try:
                if not pointer.next and pointer2==head and n==size:
                    return head.next
                elif not pointer.next and pointer2==head and size-1!=n:
                    head.next=None
                    return head
                if not pointer.next:
                    if not pointer2.next:
                        return head
                    else:
                        pointer2.next=pointer2.next.next
                        return head
            except:
                return None

