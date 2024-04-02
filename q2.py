color1 = []

for i in range(7):
    clr = input("Enter the colors: ")
    color1.append(clr)

print(color1)

color2 = color1.copy()

print(color2)

color1.remove("d")

print(color1)

color1[0] = "m"
print(color1)


for j in color1:
    print(j)

for k in color2:
    print(k)    