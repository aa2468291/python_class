from random import random

while True:
    UID = input('請輸入身份證字號')
    if UID[0].isupper() and len(UID) == 10:
        break
    else:
        print("格式錯誤，再試一次")

first = random.randint(0, 26)


rule = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num = rule[ord(UID[0]) - 65]
pre = []
total = 0

pre.append(int(num / 10))
pre.append(num % 10)

for i in UID[1:9]:
    pre.append(int(i))
# print(pre)

for j in range(len(pre)):
    total = total + (pre[j] * weight[j])

# print(UID[9])
# print(total % 10)
if int(10 - total % 10) == int(UID[9]):
    print("正確")
else:
    print("錯誤")
