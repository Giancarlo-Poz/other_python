# T=7500
# 
# hh = T//3600
# 
# hhh = str(hh)
# 
# print("ore"+hhh)
# 
# print(hh)
# 
# print( (T - T//3600 * 3600)//60 )
# 
# print( T - T//3600 * 3600 - (T - T//3600 * 3600)//60 * 60)

def solution(T):
    
    h = T//3600
    m = (T - h*3600)//60
    s = T - h*3600 - m*60
    
    hs = str(h)
    ms = str(m)
    ss = str(s)
        
    return hs + "h" + ms + "m" + ss + "s"

print(solution())