#coding: UTF-8
map={}
for line in open('./testfile.txt','r'):
    para = line.split(',')
    num = int(para[0])
    unti = int(para[1])
    map.update({num:unti})

#print map
#print map.values()
#print map[1]

f = open('./test.txt','w')
for i in range(len(map)):
    print map[i+1]
    if i==0 : f.write("%s" %map[i+1])
    else : f.write("\n%s"%map[i+1])
    
f.close()
