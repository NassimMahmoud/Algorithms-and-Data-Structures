# Implementation of  an Array data structure as a simplified type of list.

class Array(object):
    
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially
        self.initialSize=initialSize

    def __len__(self):  
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds, and
            return self.__a[n]     # only return item if in bounds
        else :raise IndexError

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds, and
            self.__a[n] = value  # only set item if in bounds

    def insert(self, item):  # Insert item at end
        if self.__nItems >= self.initialSize:
            self.__a = self.__a + [None]*self.initialSize  
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1
            

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__a[k] = self.__a[k + 1]  # right over 1
                return        # Return success flag
        raise ValueError("value not found ")  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a function
            function(self.__a[j])
            
            
Size = 10 # Max size of the array
arr = Array(Size)



for i in range(100): 
    arr.insert(i)
    

arr.traverse()
