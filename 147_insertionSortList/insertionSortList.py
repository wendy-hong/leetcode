# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Execution time: 164 ms, defeat 62.50% of all Python users
        # Memory consumption: 17 MB, defeat 11.11% of all Python users
        # Test cases passed: 19/19
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = head.next
        lastSorted = head
        while cur:
            if cur.val >= lastSorted.val:
                lastSorted = lastSorted.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSorted.next
        return dummy.next
