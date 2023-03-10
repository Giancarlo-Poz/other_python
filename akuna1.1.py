from operator import itemgetter

def rearrange(elements):

    elem_bin = [(x,bin(x)[2:].count("1")) for x in elements]

    #elem_sorted = sorted(elem_bin, key=lambda elem: elem[1] + 10**(-6) * elem[0] ) # considering 1 <= n <= 10^5
    elem_sorted = sorted(elem_bin, key=itemgetter(1,0) ) # from https://docs.python.org/3/howto/sorting.html#sortinghowto

    return [x[0] for x in elem_sorted]


el = [7,8,6,5]

print(rearrange(el))

