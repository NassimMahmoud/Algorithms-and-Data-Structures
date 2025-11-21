# n-element sequence, S, containing distinct integers that are listed in increasing order.
# Given a number k
# recursive algorithm to find two integers in S that sum to k, if such a pair
# exists. 


s=[1,3,5,8,9,10]
k=20


def sum_to_k(s):
    
    
    if len(s)==0 :
        return False
    
    if s[0] >= k  :
        return False
    else :
        if abs(k-s[0]) in s[1:] :
            return s[0],k-s[0]
        else:
           return sum_to_k(s[1:])
            

print(sum_to_k(s))

