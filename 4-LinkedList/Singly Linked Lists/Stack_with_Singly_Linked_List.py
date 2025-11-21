class Linked_Stack():
    
    class Node():
        def __init__(self,element=None,next=None):
            self.element=element
            self.next=next
            
    class Empty(Exception):
        pass
    
    def __init__(self,element=None,next=None):
        self.head= self.Node(element,next)
        self.size=0
    
    def is_empty(self):
      # Return True if the stack is empty
      return self.size == 0
  
    def __len__(self):
        # Return the number of elements in the stack
        return self.size
        
       
    def push(self,element):
        #Add element e to the top of the stack
        new_Node=self.Node(element)
        new_Node.next=self.head
        self.head=new_Node
        self.size +=1
        
    def top(self):
      #Return (but do not remove) the element at the top of the stack.

      #Raise Empty exception if the stack is empty.

      if self.is_empty():
         raise self.Empty("Stack is empty")
      return self.head.element

            
    def remove_first(self):
        #Remove and return the element from the top of the stack 
        if self.size==0 :
         raise self.Empty("Stack is empty")
        else :
         answer=self.head.element
         self.head=self.head.next
         self.size -=1
         return answer
    
    def traverse(self):
        temp=self.head
        while temp.next:
            print(temp.element,end="---> ")
            temp=temp.next
       
      
    

        
    
vv=Linked_Stack()

