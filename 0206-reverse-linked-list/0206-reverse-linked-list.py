# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr=head
        l=[]
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        dummy=ListNode(0)
        curr=dummy
        for i in range(len(l)-1,-1,-1):
            temp=ListNode(l[i])
            curr.next=temp
            curr=temp
        return dummy.next

        


        