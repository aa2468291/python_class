# 一萬以內的孿生質數

prime_list = []
twin_prime_list = []

# 檢查質數
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for j in range(1, 10001):
    if prime(j):
        prime_list.append(j)

for k in range(len(prime_list) - 1):
    if prime_list[k + 1] - prime_list[k] == 2:
        twin_prime_list.append([prime_list[k], prime_list[k + 1]])

# print(prime_list)
print(twin_prime_list)
print('共有' + str(len(twin_prime_list)) + '組孿生質數')
