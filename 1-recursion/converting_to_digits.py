# recursive function for converting a string of digits into
# the integer it represents.13531 represents the integer 13,531

def string_to_digits(s):
    
    if len(s)>0:
        
       return int(s[0]) * pow(10,len(s)-1) + string_to_digits(s[1:])
   
    #base case
    else:
        return 0
    
print(string_to_digits('13531'))

 


