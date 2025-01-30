class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        
        if  self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp    

    def pop(self):
        #case 1 :only one Node
        temp=self.head
        if temp.next is None:
            self.head=None
            return temp.val
        #case 2 :only two Nodes
        while temp.next is not None:
            temp=temp.next
        last=temp.prev
        last.next=None
        temp.prev=None
        return temp.val 
    
    def insert_start(self,val):
        new_node=Node(val)
        temp=self.head
        new_node.next=temp
        temp.prev=new_node
        self.head=new_node
        

    


            









    def __str__(self):
        doublylist=[]
        current=self.head
        while current is not None:
            doublylist.append(str(current.val))
            current=current.next
        return "-->".join(doublylist)    

    

def main():
    print("Double Linked List")
    Doubly_Linked=Doubly()
    Doubly_Linked.push(1)
    Doubly_Linked.push(2)
    Doubly_Linked.push(3)
  
    print("This is Doubly:",Doubly_Linked)
    print("This is pop func:",Doubly_Linked.pop())
    Doubly_Linked.insert_start(0)
    

    print("This is satrting insertion:",Doubly_Linked)
    



if __name__ =="__main__":
    main()