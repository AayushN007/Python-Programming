class Node:
    def __init__(self,Data):
        self.Data = Data
        self.next = None
    
class MyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_first(self,Data):
        temp = Node(Data)
        temp.next = self.head
        self.head = temp

    def add_last(self,data):
        if self.head == None:
            temp = Node(data)
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            temp = Node(data)
            curr.next = temp
    
    def delete_first(self):
        if self.head == None:
            print("LL is Empty")
        else:
            self.head = self.head.next
    
    def delete_last(self):
        if self.head == None:
            print("LL is Empty")
        else:
            curr = self.head
            while curr.next != None:
                pre=curr
                curr = curr.next
            pre.next=None
            
    def print_LL(self):
        curr = self.head
        while curr != None:
            print(curr.Data,end = "-->")
            curr = curr.next
        print("None")
            
ll = MyLinkedList()
ll.add_first(10)
ll.add_first(20)
ll.add_first(30)
ll.add_last(9)
ll.add_last(999)
ll.add_last(990)
ll.delete_last()
ll.print_LL() 