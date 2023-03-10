A=[1,2,3,2]


aa = [x/2 for x in A]

bb = list(map(lambda x: x/2, A ))

cc = [[x, y] for x in [1,2,3] for y in [1,2,3] if x != y]

print(aa,bb,cc)



def f(x):
    return x**2 + 1
    
dd = map(f, A)
dd_list = list (dd)

print(dd_list)



B = list(range(4))
C = list(range(3))

def f(x,y):
    return x**2 + y**2

dd = map(f, B, C)
dd_list = list(dd)

print(dd_list)



transpose = list(zip(aa,bb))

print(transpose)

transpose_set = list(map(set, transpose))

print(transpose_set)



print(any([False,False])) # AllTrue



ee = sum([1,3,5])

print(ee)


