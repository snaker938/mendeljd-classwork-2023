pupils = []
group1 = []
group2 = []

for i in range(0, 20):
    pupils.append(i)

for i in range(0, 20, 2):
    group1.append(pupils[i])


for i in range(1, 20, 2):
        group2.append(pupils[i])


print("GROUP 1")
print(group1)
print("")
print("GROUP 2")
print(group2)

