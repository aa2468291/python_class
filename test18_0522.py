# 考拉茲寫入TXT
import os

max_num = 0
count = 0

file = open("test.txt", "w")
file.write("    測試數字       總共         最大\n")
file.write("========================================\n")


def collatz(n):
    # print(n)

    global count
    global max_num
    count = count + 1
    if n >= max_num:
        max_num = n

    if n != 1:
        if n % 2 != 0:
            collatz(3 * n + 1)
        else:
            collatz(n // 2)
    else:
        file.write('%15s %15s %15s\n' % (test_num, count, max_num))


for test_num in range(1, 101):
    count = 0
    max_num = 0
    collatz(test_num)

# file.close()

# test_num = int(input('請輸入一個數字'))
# collatz(test_num)
# print('共有幾個數字:' + str(count))
# print('最大數字:' + str(max_num))
