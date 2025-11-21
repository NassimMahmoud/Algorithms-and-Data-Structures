#recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction



def product(m,n):
    
    if n==0:
        return 0
    
    return m + product(m,n-1)
    
    
print(product(2,25))