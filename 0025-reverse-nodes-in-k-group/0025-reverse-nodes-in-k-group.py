# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        group_prev = dummy   # node right before the current group

        while True:
            # Find the k-th node of this group (None if fewer than k remain)
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next   # leftover < k nodes -> leave as is, done

            group_start = group_prev.next   # becomes the group's tail after reversal
            group_next = kth.next           # first node after the group

            # Reverse the group; prev starts at group_next so the tail links onward
            prev, curr = group_next, group_start
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect: before-group -> new group head (old kth); move to the group's tail
            group_prev.next = kth
            group_prev = group_start