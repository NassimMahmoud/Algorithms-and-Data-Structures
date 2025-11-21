#A recursive function for computing the sum of a sequence of numbers


def linear_sum(Seq, n):
    
    if n==0:
        return 0
    else :
        return Seq[n-1] +linear_sum(Seq[:n-1],n-1) 
    
    
    
print(linear_sum([3,4,5],3))