S = "(()((())))"

def solution(S):

    stack =[]

    for el in S:
        if el == '(':
            stack.append(el)
        else: #el == ')'
            if not stack: #stack empty
                return 0
            else: #del stack[-1]
                stack.pop()
            
    if not stack: #stack empty: all parenthesis matches
        return 1
    else: #stack not empty: not enough '('
        return 0

# equivalent solution with different structure
def solution(S):

    stack =[]

    for el in S:
        if el == '(':
            stack.append(el)
            continue
        
        # el is ')'
        if not stack: #stack empty
            return 0
        else: #del stack[-1]
            stack.pop()

    # at the end
    if not stack: #stack empty: all parenthesis matches
        return 1
    else: #stack not empty: not enough '('
        return 0


print(solution(S))
            
            