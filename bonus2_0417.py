import random

rule = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
alphabet = chr(random.randint(0, 25)+65)
number = random.randint(10000000, 29999999)
num = rule[ord(alphabet) - 65]

pre = []
total = 0

pre.append(int(num / 10))
pre.append(num % 10)

for i in str(number)[0:8]:
    pre.append(int(i))
# print(pre)

for j in range(len(pre)):
    total = total + (pre[j] * weight[j])

# print(UID[9])
# print(total % 10)
check = int(10 - total % 10)
if check == 10:
    check = 0

print(pre)
print(total)

print(str(alphabet)+str(number)+str(check))
