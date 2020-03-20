# 考拉茲遞迴

max_num = 0
count = 0


def collatz(n):
    print(n)
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


n = int(input('請輸入一個數字'))
collatz(n)
print('共有幾個數字:'+str(count))
print('最大數字:'+str(max_num))
