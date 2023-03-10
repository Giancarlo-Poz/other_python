# def fib(n): # calls the function fib many times
#     """Return the sum 1 + 2 + 3 + ... + n"""
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return n + fib(n-1)

def fib2(n): # modified from your previous version to call fib2 only one time
    """Return the sum 1 + 2 + 3 + ... + n"""
    
    if n < 1:
        return 0
    
    temp1=0
    temp2=1
    i=1
    while i<n:
        temp1, temp2 = temp2, temp1 + temp2 # using one line you don't need another variable
        i = i + 1
    
    return temp2

def fib(n):    # calls the function fib only one time
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(8)
print(fib2(0))
print(fib2(1))
print(fib2(2))
print(fib2(3))
print(fib2(4))
print(fib2(5))
