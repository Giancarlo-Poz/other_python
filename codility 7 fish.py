#import random
#
# A = list(range(10))
# random.shuffle(A)
# print(A)
# B=[]
# for _ in A:
#     B.append(random.randint(0,1))
# print(B)


A = [3, 9, 0, 4, 2, 7, 6, 1, 5, 8]
B = [0, 1, 0, 1, 1, 1, 0, 1, 0, 1]

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]


def solution(A,B):

    num_init = len(A)
    num_fin = num_init

    stack = []

    for i, e in enumerate(B):
        if e==1:
            stack.append(A[i])
            continue
        
#         for _ in stack.copy():
#             num_fin -= 1
#             if A[i] > stack[-1]:
#                 del stack[-1]
#             else:
#                 break

#         for _ in stack.copy():
#             num_fin -= 1
#             if stack[-1] > A[i]:
#                 break
#             else:
#                 stack.pop()
                
            
        for _ in stack.copy():
            num_fin -= 1
            top_stack = stack.pop()
            if top_stack > A[i]:
                stack.append(top_stack)
                break




    return num_fin

print(solution(A,B))
                
                