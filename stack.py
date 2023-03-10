def solution4(S): #solution with stack improved
    
    def match(el, stack_top):
        return (el == ")" and stack_top == "(") or (el == "]" and stack_top == "[") or (el == "}" and stack_top == "{")
                
    stack = []

    for el in S:
        
        if el == "(" or el == "[" or el == "{":
            stack.append(el)
            continue
        
        if not stack: #stack empty: no matching parethesis
            return 0
        
        else:
            stack_top = stack.pop()
            
            if not match(el, stack_top):
                return 0
            
            
    if stack == []: #all parenthesis math
        return 1
    else: #not all parenthesis math
        return 0



def solution2(S): #solution with stack
    
    stack = []

    for i in range(len(S)):
        
        if S[i] == "(" or S[i] == "[" or S[i] == "{":
            stack.append(S[i])
            continue
        
        if stack == []:
            return 0
        
        elif S[i] == ")" and stack[-1] == "(":
            del stack[-1]
            continue
        
        elif S[i] == "]" and stack[-1] == "[":
            del stack[-1]
            continue
                
        elif S[i] == "}" and stack[-1] == "{":
            del stack[-1]
            continue
                
        else:
            return 0
            
    if stack == []:
        return 1
    else:
        return 0



def solution1(S): #slow solution
    S = list(S)
    while len(S)>1:
        for i in range(len(S)-1):
            Si = "".join(S[i:i+2])
            if Si == "()" or Si == "[]" or Si == "{}":
                del S[i:i+2]
                continue
            if Si == "(]" or Si == "(}"  or Si == "[)" or Si == "[}" or Si == "{)" or Si == "{]" :
                return 0

    if len(S) == 0:
        return 1
    else:
        return 0
            
        

#print("".join(S))
        
#print(solution(S))


# def simplifiable(S,i):
#     if S[i] == ")" and S[i-1] == "(":
#         return True
#     elif S[i] == "]" and S[i-1] == "[":
#         return True
#     elif S[i] == "}" and S[i-1] == "{":
#         return True
#     else:
#         return False
#
# S = list(S)
# i = 1
# while 0 < i <= len(S)/2:
#     if simplifiable(S,i):
#         del S[i-1:i+1]
#         i = i - 1
#         continue
#     else:
#         i = i + 1
# 
# if len(S) == 0:
#     #return 1
#     print("OK")
# else:
#     print("NO")
#     #return 0

def simplifiable(S,i):
    if S[i] == ")" and S[i-1] == "(":
        return True
    elif S[i] == "]" and S[i-1] == "[":
        return True
    elif S[i] == "}" and S[i-1] == "{":
        return True
    else:
        return False
    
def solution(S): # fast solution without stack
    
    if S == "":
        return 1
    if len(S)%2 == 1:
        return 0
    
    S = list(S)
    i = 0
    while 0 <= i <= len(S)//2:
        
        if S[i] == "(" or S[i] == "[" or S[i] == "{":
            i += 1
            
        elif i == 0:
            return 0
        
        elif simplifiable(S,i):
            del S[i-1:i+1]
            if S == []:
                return 1
            else:
                i -= 1
                                
        else:
            return 0
    
    if S != []:
        return 0

def solution3(S): # fast solution without stack
    
    if S == "":
        return 1
    if len(S)%2 == 1:
        return 0
    
    S = list(S)
    i = 0
    while 0 <= i <= len(S)//2:
        
        if S[i] == "(" or S[i] == "[" or S[i] == "{":
            i += 1
            
        elif i == 0:
            return 0
        
        elif simplifiable(S,i):
            del S[i-1:i+1]
            if S == []:
                return 1
            else:
                i -= 1
                                
        else:
            return 0
    
    if S != []:
        return 0

            
           
S = "((()())())"

print(S)            
print(solution4(S))