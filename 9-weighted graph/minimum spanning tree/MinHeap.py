
def key_weight(w,a,b):
    return w

class MinHeap(object):
    
 def __init__(self, size=2): # Heap constructor
  self._arr = [None] * size # Heap stored as a list/array
  self._nItems = 0 # No items in initial heap
  
 def isEmpty(self): return self._nItems == 0 # Test for empty heap
 
 def isFull(self): return self._nItems == len(self._arr)
 
 def __len__(self): return self._nItems # Number of items
 
 def peek(self): # Return item with maximum key
   return None if self.isEmpty() else self._arr[0]

 def parent(self, i): # Get index of parent in heap tree
  return (i - 1) // 2 # Item i's parent index is half of i - 1

 def leftChild(self, i): # Get index of left child in heap tree
  return i * 2 + 1 # Item i's left child is at twice i plus 1

 def rightChild(self, i): # Get index of right child in heap tree
  return i * 2 + 2 # Item i's right child -> twice i plu
 
 def _growHeap(self): # Grow the array for the heap
    current = self._arr # Store the current array
    self._arr = [None] * max(1, 2 * len(self._arr)) # Double array
    for i in range(self._nItems): # Loop over all current items &
     self._arr[i] = current[i] # copy them to the new array
 
 def _siftUp(self, i): # Sift item i up toward root to preserve
     
    if i <= 0: # heap condition. The root node, i = 0,
     return # cannot go higher, so done.
     
    while 0 < i: # While i is below the root
        
     parent = self.parent(i) # Get the index of its parent node
     
     if self._arr[parent][0] > self._arr[i][0]  : # less than that of item i,
        self._arr[i] ,self._arr[parent] =self._arr[parent] ,self._arr[i] #swap i with her parent 
        i = parent # and continue up tree
        
     else: # If parent's key is greater or equal,
        break # then we have found where item i belongs

 def insert(self, w,a,b): # Insert a new item in a heap
     
    if self.isFull(): 
     self._growHeap() 
    self._arr[self._nItems] = (w,a,b) 
    self._nItems += 1
    self._siftUp(self._nItems - 1) 
     
    
 def remove_min(self):
     
    if self.isEmpty():return None

    min_item = self._arr[0]

    # Move last element to root
    self._arr[0] = self._arr[self._nItems - 1]
    self._arr[self._nItems - 1] = None
    self._nItems -= 1

    i = 0

    while True:
        
        left = self.leftChild(i)
        right = self.rightChild(i)
        smallest = i

        # Check left child
        if left < self._nItems and self._arr[left][0] < self._arr[smallest][0]:
            smallest = left

        # Check right child
        if right < self._nItems and self._arr[right][0] < self._arr[smallest][0]:
            smallest = right

        # If node is already correct, stop
        if smallest == i:
            break

        # Swap with larger child
        self._arr[i], self._arr[smallest] = self._arr[smallest], self._arr[i]
        
        i = smallest
    
    return min_item         


vv=MinHeap()

vv.insert(345,3,3)
vv.insert(12,1,2)
vv.insert(13,3,4)
vv.insert(99,3,4)
vv.insert(0,3,4)
vv.insert(18,3,4)



print(vv._arr)

vv.remove_min()

print(vv._arr)