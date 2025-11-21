# recursive function for computing the nth Harmonic number,


def harmonic(n):
    
    if n==0:
        return 0
    
    return (1/n) + harmonic(n-1)

print(harmonic(5))