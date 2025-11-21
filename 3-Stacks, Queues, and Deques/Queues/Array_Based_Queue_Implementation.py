class Empty(Exception):
    # Error attempting to access an element from an empty container
    pass

class ArrayBasedQueue:
    
    Default_Capacity = 10  # moderate capacity for all new queues 
    
    def __init__(self):
        # Create an empty queue
        self.data = [None] * ArrayBasedQueue.Default_Capacity
        self.size  =  0 # number of elements in the queue
        self.front =  0 # index of the front element
        self.rear  =  0 # index of the next available slot at the back
     
    def __len__(self):
        # Return the number of elements in the queue
        return self.size 
 
    def is_empty(self):
        # Return True if the queue is empty
        return self.size == 0 
  
    def first(self):
        # Return (but do not remove) the element at the front of the queue.
        # Raise Empty exception if the queue is empty.
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front]
    
    def resize(self, cap):        # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self.data           # keep track of existing list
        self.data = [None] * cap  # allocate list with new capacity
        walk = self.front
        for k in range(self.size):     # only consider existing elements
            self.data[k] = old[walk]   
            walk += 1            
            
        self.rear=self.size # rear  has been  realigned to 0
        self.front=0        # front has been realigned  to 0
 
 
    def enqueue(self, e):
        
        """ Add an element to the back of queue."""
        if self.rear == len(self.data):
            self.resize(2 * len(self.data))  # double the array size
        self.data[self.rear] = e
        self.size += 1
        self.rear += 1
        
    def dequeue(self):

        # Remove and return the first element of the queue (i.e., FIFO).
        # Raise Empty exception if the queue is empty.
        
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self.data[self.front]  # retrieve the front element
        self.data[self.front] = None   
        self.front +=  1  # advance front index circularly
        self.size  -=  1
        return answer 
 
       
   

c=ArrayBasedQueue()




