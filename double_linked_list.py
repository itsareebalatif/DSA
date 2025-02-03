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
        if temp is None:
            return
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

    def insert(self,index,val):
        new_node=Node(val)
        temp=self.head
        # If the list is empty and inserting at index 0
        if self.head is None:
            self.head=new_node
            return
        # If inserting at the beginning (index 0)
        if  index==0:
            self.head=new_node
            new_node.next=temp
            temp.prev=new_node
            return
        counter=0
        previous=None
        while temp  is not None and counter<index:
            previous=temp
            temp=temp.next
            counter+=1
        # if index not found enter at last    
        if temp is None:
            previous.next=new_node
            new_node.prev=previous
            return  
        # Inserting at the middle  
        previous.next=new_node   
        new_node.prev=previous

        new_node.next=temp
        if temp is not None:
           temp.prev=new_node
        return
        
    def remove(self,value):
        temp=self.head
        if temp.val==value:
            if temp.next is not None:
                print("Case 1 to remove from 0 index")
                self.head=temp.next
                self.head.prev=None
                return
            print("case 2 to remove from 0 index ")    
            self.head=temp.next 
            return 

        last=None
        while temp is not None:
            if temp.val==value:
                break
            last=temp
            temp=temp.next

        if temp is None:
            return
        if temp.next is None:
            last.next=temp.next
            return
        else:
            last.next=temp.next
            temp.next.prev=last  
            return  





            




        

    


            









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
    Doubly_Linked.insert(2,11)
    Doubly_Linked.insert(19,12)
    
  
    print("This is Doubly after insert :",Doubly_Linked)
    Doubly_Linked.remove(1)
    print("This is Doubly after remove :",Doubly_Linked)
    print("This is pop func:",Doubly_Linked.pop())
    Doubly_Linked.insert_start(0)
    print("This is satrting insertion:",Doubly_Linked)

    



if __name__ =="__main__":
    main()