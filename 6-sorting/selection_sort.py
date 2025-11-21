

def selection_sort(A):
    
    for i in range(0,len(A)):
        min=i
        for j in range(i+1,len(A)):
            if A[j] < A[min]:
               min=j
        A[i],A[min]=A[min],A[i]
    return A
      
print(selection_sort([8,3,2,3,1,2,-5]))