class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None

class Doubly_linked_list:
    def __init__(self):
        self.head=None

    def push(self,value):
        new_Node=Node(value)
        if self.head is None:
            self.head=new_Node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_Node
        new_Node.prev=temp
        return
    
    def reverse(self):
        extra_set=[]
        if self.head is None:
            return "Empty Linked List"
        temp=self.head
        while temp is not None:
            extra_set.append(temp.val)
            temp=temp.next
        temp=self.head
        while temp is not None:
            temp.val=extra_set.pop() 
            temp=temp.next
        return        
 







    def __str__(self):
        doublylist=[]
        current=self.head
        while current is not None:
            doublylist.append(str(current.val))
            current=current.next
        return "-->".join(doublylist)         

def main():
    print("Reversed Doubly Liked List")
    Doubly=Doubly_linked_list()
    Doubly.push(1)
    Doubly.push(2)
    Doubly.push(3)
    print(Doubly)
    Doubly.reverse()
    print(Doubly)

if __name__=="__main__":
    main()    