A = [1,5,2,1,4,0]


# A_enum = list(enumerate(A))
# 
# A_sort = sorted(A)
# 
# print(A)
# #print(A_sort)
# print(A_enum)
# 
# print(sorted(A_enum, key=lambda el: el[1], reverse=True))
#

def solution (A):
    
    def test_inters(pos1,r1,pos2,r2):
        return r1 + r2 >= pos2 - pos1

    n_inters = 0

    for pos1, r1 in enumerate(A[:-1]):
        for el, r2 in enumerate(A[pos1+1:]):
            pos2 = pos1 + el + 1
            if test_inters(pos1,r1,pos2,r2):
                n_inters = n_inters + 1
#                 if n_inters > 10000000:
#                     return -1

    return n_inters

def solution1 (A):
    
    def test_inters(pos1,r1,pos2,r2):
        return r1 + r2 >= pos2 - pos1

    n_inters = 0

    for pos1, r1 in enumerate(A[:-1]):
        for pos2, r2 in enumerate(A[pos1+1:],start=pos1+1):
            if test_inters(pos1,r1,pos2,r2):
                n_inters = n_inters + 1
#                 if n_inters > 10000000:
#                     return -1

    return n_inters




#B=[0]*len(A)
# for i, el in enumerate(A):
#     B[i] = i - el


def solution2(A):

    B=[]
    for i, el in enumerate(A):
        B.append(i-el)

    n_inters = 0

    for i, el_A in enumerate(A):
        #n_inters = n_inters + sum(1 for el_B in B[i+1:] if el_B <= i + el_A)
        n_inters = n_inters + len([el_B for el_B in B[i+1:] if el_B <= i + el_A])
        
        if n_inters > 10000000:
            return -1

        
    return n_inters



