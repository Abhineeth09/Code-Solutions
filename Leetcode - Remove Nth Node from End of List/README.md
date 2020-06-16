## 19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Solution:

Instead of one pointer, we could use two pointers. The first pointer advances the list by 
n
+
1
n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by 
n
n nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the 
n
nth node counting from the last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.