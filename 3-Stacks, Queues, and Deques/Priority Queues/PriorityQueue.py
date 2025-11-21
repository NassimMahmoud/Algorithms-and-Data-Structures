# Implement a Priority Queue data structure using a Python list

class PriorityQueue():
    
    def __init__(self,size):
        self.max_size=size
        self.queue=[None] * size
        self.nitems=0

    def priority(self,item):
        return item
        
    def isEmpty(self): return self.nitems == 0
    
    def isFull(self): return self.nitems == self.max_size
    
    def __len__(self):return self.__nItems

    
    def insert(self, item):
        
        if self.isFull(): # priority queue if not full
            raise Exception("Queue overflow")
     
        self.queue[self.nitems]=item # append at last item
        self.nitems +=1     #increment the size 
        
        index= self.nitems-1
        
        while  index > 0 and self.queue[index] < self.queue[index-1]:
            
            #swap if the newly added item has higher priority
            self.queue[index] ,self.queue[index-1]=self.queue[index-1] ,self.queue[index] #swape 
            index -=1
              
    def remove(self): # Return front item of priority
        if self.isEmpty(): # queue, if not empty, & remove
            raise Exception("Queue underflow")
   
        self.nitems -= 1 # One fewer item in queue
        front = self.queue[self.nitems] # Store frontmost item
        self.queue[self.nitems] = None # Remove item reference
        return front
            
    def __str__(self): # Convert pri. queue to string
        ans = "[" # Start with left bracket
        for i in range(0,self.nitems, 1): # Loop from front
            if len(ans) > 1: # Except next to left bracket,
                ans += ", " # separate items with comma
            ans += str(self.queue[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans
            
            
        
        
            
        
        
cc=PriorityQueue(10)





        

print(cc)
        
        
        
        