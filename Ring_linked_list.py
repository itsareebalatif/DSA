def main():
    print("Circular linked list")

class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        

class Ring:
    def __init__(self):
        self.head=None

    def _get_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            return self.head
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next

        return temp        

    def insert(self,index,value):
        new_node=Node(value)
        last=self._get_last()
        temp=self.head
        #case 1.0
        if self.head is None:
            if  index>0:
               raise IndexError ("index out of bound")
            self.head=new_node
            new_node.next=self.head
            return
        #case 1.1
        if index==0:
            new_node.next=self.head
            self.head=new_node
            if temp.next is None:
                self.head.next=self.head
            else:
                last.next=new_node
            return 
        previous=None
        counter=0
        #case 2.0
        while  counter<index:
            previous=temp
            temp=temp.next
            counter+=1 
        previous.next=new_node
        new_node.next=temp 

    def remove(self,value):
        if self.head is None:
            return 
        temp=self.head
        last=self._get_last
        if temp.val==value:
            if temp.next is None:
                self.head=None
            self.head=temp.next
            last.next=self.head
        previous=temp
        temp=temp.next 
        while temp!=self.head:
            if temp.val==value:
                break
            previous=temp
            temp=temp.next 
        if temp==self.head :
            return     
        previous.next=temp.next      






    def __str__(self):
        if self.head is None:
            return "Empty List"
        circular = []
        current = self.head
        while True:
            circular.append(str(current.val))
            current = current.next
            if current == self.head:
                break  
        return "-->".join(circular) + "-->"  # Fixed variable name

     
def main():
    print("Circular linked list")
    Rings=Ring()
    Rings.insert(0,1)
    Rings.insert(0,2)
    Rings.insert(1,3)
    Rings.insert(7,5)
    print(Rings)
    Rings.remove(9)
    print(Rings)


if __name__=="__main__":
    main()