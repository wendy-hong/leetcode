# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers_sol1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Execution time: 56 ms, defeat 59.98% of all Python users
        # Memory consumption: 15 MB, defeat 46.69% of all Python users
        # Test cases passed: 1568/1568
        if l1.val == 0 and l1.next == None:
            return l2
        if l2.val == 0 and l2.next == None:
            return l1
        l = ListNode(0)
        tmp = l
        carry = 0
        while l1 and l2:
            cur = l1.val + l2.val + carry
            carry = cur // 10
            tmp.next = ListNode(cur % 10)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        if not l1:
            while l2:
                if carry:
                    cur = l2.val + carry
                    tmp.next = ListNode(cur % 10)
                    carry = cur // 10
                else:
                    tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        elif not l2:
            while l1:
                if carry:
                    cur = l1.val + carry
                    tmp.next = ListNode(cur % 10)
                    carry = cur // 10
                else:
                    tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
        if carry:
            tmp.next = ListNode(carry)
        return l.next

    def addTwoNumbers_sol2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time: O(max(m,n)), Space: O(1)
        # Execution time: 60 ms, defeat 37% of all Python users
        # Memory consumption: 14.8 MB, defeat 95% of all Python users
        # Test cases passed: 1568/1568
        l = ListNode(0)
        cur = l
        carry = 0
        while l1 or l2:
            vall1 = l1.val if l1 else 0
            vall2 = l2.val if l2 else 0
            sum = vall1 + vall2 + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return l.next
