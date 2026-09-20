# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)   # sentinel so removing head needs no special case
        fast = slow = dummy

        # Advance fast n+1 steps ahead, creating an n-node gap between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast falls off the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # slow is now just before the target node -> unlink it
        slow.next = slow.next.next

        return dummy.next