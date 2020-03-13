n = int(input('請輸入一個數字'))

print(n)
count = 1


while n != 1:
    count = count + 1

    if n % 2 != 0:
        n = 3 * n + 1
        print(int(n))
    else:
        n = n / 2
        print(int(n))

    # print(result)

print('總共有：'+str(count)+'個數字')