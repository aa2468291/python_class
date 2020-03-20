# 判斷是否符合中心十邊形質數
def ten(ans):
    k = 1
    while 5 * (k * k + k) + 1 <= ans:
        if 5 * (k * k + k) + 1 == ans:
            return True
        k = k + 1

    return False


# 檢查質數
def prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        i = i + 1
        if n % i == 0:
            return False
        return True


for i in range(2, 10000):
    if ten(i) and prime(i):
        print(i)
