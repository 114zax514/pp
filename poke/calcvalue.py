#coding: utf-8
#s:種族値 e:努力値 b:性格補正
def calcV(s,e,b):
    if(e>3) : ev = e / 8 + 1
    else : ev = 0
    if(b==1) : v = ( s + 20 + ev ) * 1.1
    elif(b==2) : v = ( s + 20 + ev ) * 0.9
    else : v =  s + 20 + ev  

    return int(v)

print calcV(100,252,1)
print calcV(100,252,0)
