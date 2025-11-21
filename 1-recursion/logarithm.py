# recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division

def logarithm(n):
    
    count=0
   
    if n>1:
        
        n=n//2
        count=count+1 
        return count + logarithm(n)
    
    else :
        
        return 0
        
        
    
print(logarithm(32))

