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
        
        if self.head is None:
            if  index>0:
               raise IndexError ("index out of bound")
            self.head=new_node
            new_node.next=self.head
            return
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
        
        while  counter<index:
            previous=temp
            temp=temp.next
            counter+=1
           
        previous.next=new_node
        new_node.next=temp                       


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
    print(Rings)
    Rings.insert(1,3)
    print(Rings)


if __name__=="__main__":
    main()