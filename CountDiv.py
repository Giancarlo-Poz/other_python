A = 10
B = 15
K = 5

def solution (A,B,K):
    first = A - (A%K) + K
    last = B - (B%K)

    sol = (last - first) // K + 1
    
    if A%K == 0:
        return sol + 1
    else:
        return sol


print(solution(A,B,K))

print(list(range(A,B,K)))