
A = [2, 4, 50,51,53,500,0]
 
def solution(A):
    
    A = sorted(A)
        
    def cond(el_i,el_j,el_k):
        return el_i + el_j > el_k

    for el in A.copy(): #delete negative elements
        if el <= 0:
            del A[0]
        else:
            break
    
    lenA = len(A)
    
    el_old_i = el_old_j = el_old_k = 0
    
    for i, el_i in enumerate(A):
        if el_i == el_old_i:
            continue #already checked so skip
        else:
            for j, el_j in enumerate(A[i+1:lenA-1]):
                if el_j == el_old_j and el_i == el_old_i:
                    continue
                else:
                    for k, el_k in enumerate(A[i+1:][j+1:]):
                        if el_k == el_old_k and el_j == el_old_j and el_i == el_old_i:
                            continue
                        else: #will check triangle so we fixed values
                            el_old_i = el_i                    
                            el_old_j = el_j
                            el_old_k = el_k
                            
                        if cond(el_i,el_j,el_k):
                            if cond(el_j,el_k,el_i) and cond(el_k,el_i,el_j):
                                return 1
                        else:
                            break
    return 0


def solution1(A):
    
    def cond(a,b,c):
        return a+b>c
    
    A = sorted(A)
    
    for i, el in enumerate(A):
        if el>0:
            del A[:i]
            break
    
    for i, el in enumerate(A[:-2]):
        if cond(A[i],A[i+1],A[i+2]):
            return 1
    
    return 0
            

print(solution1(A))


