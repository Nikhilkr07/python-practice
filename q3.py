

l1 = [1,2,3]
l2 = [4,5,6]

print(l1)
print(l2)

l3 = l1.copy() + l2.copy()

print(l3)

l1.append(10)
print(l1)

l2.remove(5)
print(l2)

for i in l1:
    print(i)
print()
for i in l2:
    print(i)
print()
for i in l3:
    print(i,end=" ")


print(len(l1))