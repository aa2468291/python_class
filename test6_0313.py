x = 1
y = 2
n = int(input('請輸入A[n]'))

for i in range(n - 1):
    z = 3 * y + 5 * x + 1
    x = y
    y = z

print(z)
