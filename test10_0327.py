# list 九九乘法表

listA = []
listB = []

for i in range(1, 10):
    for j in range(1, 10):
        listA.append(str(i) + 'x' + str(j) + '=' + str(i * j))
    listB.append(listA[:])
    listA.clear()

print(listB)
