# Given an unsorted sequence, S, of integers and an integer k

# recursive algorithm for rearranging the elements in S so that all elements

# less than or equal to k come before any elements larger than k

s=[1,2,3,4,5,4,3,9,0,-1,-2,-3]

k=1

def rearrange(s):
    
    #base case
    if len(s)==1:
        return [s[0]]
    
    else :
        
        if s[0] <= k :                       
            
            return [s[0]] + rearrange(s[1:])
        
        if s[0] >= k and s[-1] <=k :        
            
            s[0],s[-1]=s[-1],s[0]
            
            return [s[0]] + rearrange(s[1:])
        
        if s[0] >= k and s[-1] >= k :     
            
            return rearrange(s[0:-1]) +[s[-1]]
            
        
    
print(rearrange(s))
    
