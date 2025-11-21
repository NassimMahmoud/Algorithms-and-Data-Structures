#  recursive algorithm for finding the maximum element
#  in a sequence, S, of n elements


s=[4,5,6,2,1,4,5,12,1,2,3]


def find_maxim(data,start,stop):
    
    mid=(start+stop)//2
    
    if start == stop:
        
        return
    
    if stop==start+1:
        
        return data[start] if data[start]>data[stop] else data[stop]

    
    max1=find_maxim(data,start,mid)
    
    max2=find_maxim(data,mid,stop)
    
    if max1> max2:
        return max1
    else:
        return max2
    
    

print(find_maxim(s,0,len(s)-1))


