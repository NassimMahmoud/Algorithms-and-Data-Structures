class DoublyLinkedList():
    
    class Node:
        
        def __init__(self,data,next,prev):
            self.data=data
            self.next=next
            self.prev=prev
            
            
    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer # trailer is after header
        self.trailer.prev = self.header # header is before trailer
        self.size=0
        
    def append(self,data):
        
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
            

    def prepend(self,data):
        
        new_node=self.Node(data,None,None)
        
        if self.is_empty():
            new_node.prev=self.header
            new_node.next=self.trailer
            self.header.next=new_node
            self.trailer.prev=new_node
        else:
            temp=self.header.next
            new_node.prev=self.header
            new_node.next=temp
            self.header.next=new_node
            temp.prev=new_node
            
        self.size +=1
    
    def delete(self,data):
        
        # delete the first occurence
        
        node_to_delete=None
        begin_at=self.header.next
        
        while begin_at.data != data :
            begin_at=begin_at.next
            
        node_to_delete=begin_at
        node_to_delete.data=None
        self.size -=1 
    
    def traverse(self):
        temp1=self.size
        temp2=self.header
        data=[]
        
        while temp1 > 0:
            if temp2.next.data !=None : data.append(str(temp2.next.data))
            temp1 -=1
            temp2=temp2.next   
        return ["header"] + data +["trailer"]
    
            
    def is_empty(self):
        return self.size==0
    
    def len (self):
     # Return the number of elements in the list
     return self.size
 
    
    
                
cc=DoublyLinkedList()
cc.append(7)
cc.append(8)
cc.append(8)



cc.prepend(8)
cc.prepend(9)


print(cc.traverse())






