# recursive Python function that rearranges a sequence of integer
# values so that all the even values appear before all the odd values 



def rearrange(s):
    
    #base case
    if len(s)==1:
        return [s[0]]
    
    else :
        
        if s[0] %2 ==0 :                         #[4,....,2]
            
            return [s[0]] +rearrange(s[1:])
        
        if s[0] %2 !=0 and s[-1] %2==0 :         #[3,....4]
            
            #swap first and last elements
            s[0],s[-1]=s[-1],s[0]
            
            return [s[0]] +rearrange(s[1:])
        
        if s[0] %2 !=0 and s[-1] %2!=0 :         #[3,.....,3]
            
            return rearrange(s[0:-1]) +[s[-1]]
            
        
    
print(rearrange(list(range(10))))
    
    
    
