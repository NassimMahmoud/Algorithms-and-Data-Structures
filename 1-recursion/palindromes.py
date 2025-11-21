# a recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse



def plandirome(s):
    
    if len(s)==1 or len(s)==0:
        return True
    else :
        if s[0] == s[-1]:
           return  plandirome(s[1:-1])
        else :
            return False
            
        
print(plandirome("raar"))
    