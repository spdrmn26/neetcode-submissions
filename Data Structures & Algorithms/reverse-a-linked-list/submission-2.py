# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The gold standard expectation for this problem is to reverse the list 
        # in-place in a single pass. You don't need to reach the end first; you 
        # just need to start at the head and flip the arrows backwards as you 
        # walk down the list.

        # The Optimal Pattern: In-Place Reversal (Three Pointers)
        # Because it's a singly-linked list, we can only move forward. If we 
        # simply change a node's next pointer to point to the previous node, 
        # we completely lose our connection to the rest of the list!

        # To solve this, we track three variables as we walk down the list:

        # prev: The node we just came from (starts as None because the new 
        # tail will point to None).

        # curr: The node we are currently looking at.

        # nxt: A temporary placeholder to save the rest of the list before 
        # we sever the connection.

        prev = None
        curr = head

        while curr:
            # 1. SAVE: Store the next node so we don't lose the rest of the list
            nxt = curr.next

            # 2. FLIP: Reverse the pointer of the current node
            curr.next = prev

            # 3. SHIFT: Move our pointers one step forward for the next loop
            prev = curr
            curr = nxt

        # At the end of the loop, curr is None, making prev the new head
        return prev
