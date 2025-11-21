# Recursive Python function for factorial calculation


def factorial(n):
    
    # Base case: if n is 0, return 1
    if n == 0:
        
        return 1  
      
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)


N = 5
result = factorial(N)
print(result)