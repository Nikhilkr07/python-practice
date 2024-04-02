import math
l1 = [1,2,3,4,5,6,7,8,9,10]
p = []
np = []
f = False

for i in l1:
    if i == 1 or i == 0:
        print()
    else:
        f = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            f = False
            break
    if(f):
        p.append(i)
    else:
        np.append(i)    

print(l1)                
print(p)                
print(np)                
