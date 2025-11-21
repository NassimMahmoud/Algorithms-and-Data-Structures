
#Reversing the elements of a sequence using linear recursion

def reverse(Seq,n):
    
    #n=length of the sequence
    
    
    if n==1:
        
        return Seq
    
    if n==2:
        
        return [Seq[1],Seq[0]]
    
    else: 
        
       return [Seq[n-1]] + reverse(Seq[1:n-1],n-2) +[Seq[0]]
    
       
print(reverse([6,5,7],3))