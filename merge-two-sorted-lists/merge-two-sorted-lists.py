# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = None
        head = None
        while l1 and l2:
            if l1.val<=l2.val:
                if not sortedList:
                    sortedList = l1
                    head = sortedList
                    l1 = l1.next
                    sortedList.next = None
                else:
                    sortedList.next = l1
                    l1 = l1.next
                    sortedList = sortedList.next
                    sortedList.next = None
            else:
                if not sortedList:
                    sortedList = l2
                    head = sortedList
                    l2 = l2.next
                    sortedList.next = None
                else:
                    sortedList.next = l2
                    l2 = l2.next
                    sortedList = sortedList.next
                    sortedList.next = None
        print(l1,l2)
        if l1:
            if not sortedList:
                head = l1
            else:
                sortedList.next = l1
        if l2:
            if not sortedList:
                head = l2
            else:
                sortedList.next = l2
        return head
        
        