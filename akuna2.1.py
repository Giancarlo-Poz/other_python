wallPositions = [1,4,7]
wallHeights = [4,3,3]


def triangleHeight(start, end, hStart, hEnd):
    basetriangleHeight = (end + hEnd) - (start - hStart) #triangle base length
    return basetriangleHeight//2 #edges at pi/4

def maxHeight(wallPositions, wallHeights):
    max = 0
    
    for i in range(len(wallPositions)-1):
        mudHeight = triangleHeight(wallPositions[i],wallPositions[i+1],wallHeights[i],wallHeights[i+1])
        if mudHeight > max:
            max = mudHeight
        
    return max

def maxHeight1(wallPositions, wallHeights):
    max = 0
    
    for wp1, wp2, wh1, wh2 in zip(wallPositions,wallPositions[1:],wallHeights,wallHeights[1:]):
        
        print(wp1,wp2,wh1,wh2)
        
        mudHeight = triangleHeight(wp1,wp2,wh1,wh2)
        if mudHeight > max:
            max = mudHeight
        
    return max


print(maxHeight(wallPositions, wallHeights))
print(maxHeight1(wallPositions, wallHeights))
# 
# print(list(zip(wallPositions,wallPositions[1:],wallHeights,wallHeights[1:])))
# 
# for el2idx, el1 in enumerate(wallPositions, 1):
#     
#     print("el2idx = ", el2idx,"el1 = ", el1)
#     
#     #el2 = l[el2idx]