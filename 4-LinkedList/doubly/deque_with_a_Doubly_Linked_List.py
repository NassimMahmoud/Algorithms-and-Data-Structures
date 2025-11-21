class LinkedDeque():
    
    class Node:
        
        def __init__(self,data,next,prev):
            self.data=data
            self.next=next
            self.prev=prev
            
    class Empty(Exception):
        pass
            
            
    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer # trailer is after header
        self.trailer.prev = self.header # header is before trailer
        self.size=0
    
    def is_empty(self):
        return self.size==0
    
    def len (self):
     # Return the number of elements in the list
     return self.size
    
    def first(self):
        if self.is_empty():
            raise self.Empty("list is empty")
        else :
            return self.header.next.data
            
    
    def last(self):
        if self.is_empty():
            raise self.Empty("list is empty")
        else :
            return self.trailer.prev.data
    
    def insert_first(self,data):
        new_node=self.Node(data,None,None)

        if self.is_empty():
            new_node.prev=self.header
            new_node.next=self.trailer
            self.header.next=new_node
            self.trailer.prev=new_node
        else :
            temp=self.header.next
            new_node.prev=self.header
            new_node.next=temp
            self.header.next=new_node
            temp.prev=new_node
            
        self.size +=1
          
      
    def insert_last(self,data):
         # insert at last position
        new_node=self.Node(data,None,None)
        
        if self.is_empty():
            new_node.prev=self.header
            new_node.next=self.trailer
            self.header.next=new_node
            self.trailer.prev=new_node
        else:
            insert_at=self.trailer.prev    
            insert_at.next=new_node
            new_node.prev=insert_at
            new_node.next=self.trailer
            self.trailer.prev=new_node
                           
        self.size +=1
    
    def delete_first(self):
        
        if self.is_empty():
            raise self.Empty("empty") #[header,12,trailer]
        
        else:
            
            delete_at=self.header.next 
            self.header.next=delete_at.next
            delete_at.next.prev=self.header
                           
        self.size -=1
    
    def delete_last(self):
        if self.is_empty():
            raise self.Empty("empty") #[header,12,trailer]
        
        else:
            
            delete_at=self.trailer.prev
            self.trailer.prev=delete_at.prev
            delete_at.prev.next=self.trailer
                           
        self.size -=1
    
    def traverse(self):
        data=[]
        temp=self.header.next
        while temp.data:
            data.append(str(temp.data))
            temp=temp.next 
        return "header--> " + "--> ".join(data)  +"--> trailer"
            
cc=LinkedDeque()

cc.insert_first(10)
cc.insert_last(20)

print(cc.traverse())    