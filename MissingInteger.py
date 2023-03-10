#A = [1, 3, 6, 4, 1, 2]
A = [1, 3, 6, 4, 1, 2]

def solution(A):
    Asorted = sorted(set(A))

    if Asorted[-1] < 1:
        return 1
        
    for i, e in enumerate(Asorted):
        if e > 0:
            ind = i
            break
        
    for i, e in enumerate(Asorted[ind:]):
        if e > i+1:
            return i+1
    else:
        return i+2

        
print(solution(A))