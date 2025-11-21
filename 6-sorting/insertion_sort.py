# insertion sort implemetation  

def insertion_sort(s):
    
    for i in range(1,len(s)):
        
        for j in range(i,0,-1):
            
            if s[j] < s[j-1]:
                
                s[j-1],s[j]=s[j],s[j-1]
    return s
        
    
    

print(insertion_sort([1,2,2,9,0,-1]))

  

  



