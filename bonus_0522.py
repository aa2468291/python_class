# 考拉茲寫入TXT
import os

max_num = 0
count = 0
lines = ""
final_number = 0
check = False
filepath = "test.txt"


def read_file():
    global lines
    global final_number
    file_r = open("test.txt", "r")
    lines = file_r.readlines()
    final_number = int(lines[len(lines) - 1].split()[0])
    file_r.close()


# 檢查檔案是否存在
if os.path.isfile(filepath):
    check = True
    read_file()

file_w = open("test.txt", "w")
file_w.write("    測試數字       總共         最大\n")
file_w.write("========================================\n")

if check:
    for line in lines[2:len(lines)]:
        file_w.write(line)


def collatz(n):
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
        file_w.write('%15s %15s %15s\n' % (test_num, count, max_num))


for test_num in range(final_number + 1, final_number + 101):
    count = 0
    max_num = 0
    collatz(test_num)

file_w.close()
