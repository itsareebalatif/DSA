

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
         
      




def main():
   Linked_list=Linkedlist()
   Linked_list.push(2)
   Linked_list.push(3)
   Linked_list.push(4)
   Linked_list.push(5)
   print(Linked_list)
   print("This is the length of our linked list:",Linked_list.leng())
   print(Linked_list.index_val(5))
   





if __name__=="__main__":
   main()
   