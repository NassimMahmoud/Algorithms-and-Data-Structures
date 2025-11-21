#python implimentation of Singly Linked List

class Singly_Linked_List():
    
    class Node():
        def __init__(self,element=None,next=None):
            self.element=element
            self.next=next
    
    def __init__(self,element=None,next=None):
        self.head= self.Node(element,next)
        self.size=0
        
        
    def insert(self,element):
        new_Node=self.Node(element)
        new_Node.next=self.head
        self.head=new_Node
        self.size +=1

            
    def remove_first(self):
        if self.size==0 :
         return
        else :
         self.head=self.head.next
         self.size -=1
    
    def traverse(self):
        temp=self.head
        while temp.next:
            print(temp.element,end="---> ")
            temp=temp.next
       
      
    

        
    
vv=Singly_Linked_List()


