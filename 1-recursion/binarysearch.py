# a recursive function for binary search


def binary_search(data,target,start,stop):
    
    if start==stop:
        return False
    
    mid=(start+stop)//2
        
    if data[mid]==target:
        return True
    
    elif target < data[mid]:
        
       return binary_search(data,target,start,mid)
   
    else:
        
      return binary_search(data,target,mid+1,stop)

        
#test the binary search function
data=[-5,-3,0,1,4,6,8,10,15,23,45,67,89]                    
    
print(binary_search(data,90,0,len(data)))

