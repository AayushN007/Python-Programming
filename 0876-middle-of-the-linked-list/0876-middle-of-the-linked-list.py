# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        curr=head
        count=0
        while curr!=None:
            curr=curr.next
            count+=1
        mid=count//2
        curr=head
        for i in range(mid):
            curr=curr.next
        return curr