
def bubble_sort(A):
    
    
    for i in range(len(A)-1,-1,-1):
        print(i)
        max=i
        for j in range(i):
            if A[j] > A[max]:
               max=j
        A[i],A[max]=A[max],A[i]
        
    return A

        
        
bubble_sort([8,3,2,3,1,2,-5])