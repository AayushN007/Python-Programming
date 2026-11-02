class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = head
        k = k % length
        curr = head
        for i in range(length - k -1):
            curr = curr.next
        res = curr.next
        curr.next = None
        return res