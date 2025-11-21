#Summing the elements of a sequence using binary recursion


def binary_sum(Seq, start,stop):
    
    
    if start==stop:
            
        return 0
     
    else :
            
        mid=(start+stop)//2
           
        return binary_sum(Seq,start,mid) + Seq[mid] + binary_sum(Seq,mid+1,stop)
    
    
    
print(binary_sum([3,4,4,5,6],0,5))

