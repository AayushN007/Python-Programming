# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        ll1=list1
        ll2=list2
        l1=[]
        while ll1!=None:
            l1.append(ll1.val)
            ll1=ll1.next
        while ll2!=None:
            l1.append(ll2.val)
            ll2=ll2.next
        l1.sort()
        
        dummy=ListNode(0)
        curr=dummy
        for i in range(len(l1)):
            temp=ListNode(l1[i])
            curr.next=temp
            curr=temp
        return dummy.next



        