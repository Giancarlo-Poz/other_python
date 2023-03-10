import collections

# from collections import Counter

list1 = ['x','y','z','x','x','x','y','z']

count = collections.Counter(list1)

print(count["x"])

count["x"] = 0

print(count)

count.update(["a","b","b"])

print(count)

elem = list(count)

val = []
for i in elem:
    val.append(count[i])

print(elem, val)

print(count.most_common())

