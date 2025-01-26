

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



def main():
   Linked_list=Linkedlist()
   Linked_list.push(2)
   Linked_list.push(3)
   print(Linked_list)





if __name__=="__main__":
   main()
   