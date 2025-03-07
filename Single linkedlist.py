

class Node:
   def __init__(self,data):
      self.val=data
      self.next=None

class Linkedlist:
   def __init__(self):
      self.head=None

   def push(self,val):
      new_node=Node(val)
      if self.head is None:
         self.head=new_node
         new_node.next=None
         return
      temp=self.head
      while temp.next is not None:
         temp=temp.next
      temp.next=new_node
      new_node.next=None

   def __str__(self):
      
      listed=[]
      current=self.head
      while current is not None:
         listed.append(str(current.val))
         current=current.next
      return "->".join(listed)   
   
   def leng(self):
      temp=self.head
      counter=0
      while temp is not None:
         temp=temp.next
         counter+=1
      return counter   
   
   def index_val(self,value):
      temp=self.head
      counter=0
      while  temp is not None:
         temp=temp.next
         counter+=1
         if temp.val==value :
            return counter
         
      
   def get_middle(self):
      
      length=self.leng()
      
      middle=length//2
      temp=self.head
      
      while middle:
         temp=temp.next
         middle-=1
         
         
      return temp.val   
   

   def remove(self,val):
      temp=self.head
      if self.head is None:
         return
      
      if temp.val==val:
         self.head=temp.next
         temp=None
         print("case 1 remove starting node")
         return

      prev=None
      while temp is not None:
         if temp.val==val:
            prev.next=temp.next
            temp=None
            print("case 2 remove inbetwen node")
            return
         prev=temp
         temp=temp.next
      print("case 3 val not found ")   
      return "not found" 
   

   def deleteNode(self,x):
    # Code here
    temp=self.head
    if x==1:
        self.head=temp.next
        temp=None
        return 
    prev=None
    counter=1
    while temp is not None:
        if counter==x:
            prev.next=temp.next
            temp=None
            
            return 
        counter+=1    
        prev=temp
        temp=temp.next
    return   



      



def main():
   Linked_list=Linkedlist()
   Linked_list.push(2)
   Linked_list.push(3)
   Linked_list.push(4)
   Linked_list.push(5)
   Linked_list.push(6)
   print(Linked_list)
   print("This is the length of our linked list:",Linked_list.leng())
   print(f"The index of given no you gave:",Linked_list.index_val(4))
   Linked_list.get_middle()
   print("This is middle of linked list:",Linked_list.get_middle())
   print(Linked_list.remove(2))
   print(Linked_list)

   print(Linked_list.deleteNode(1))
   print(Linked_list)
   





if __name__=="__main__":
   main()
   