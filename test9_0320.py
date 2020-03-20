# 遞迴取最大公因數


def gcd(a, b):
    if a % b != 0:
        left = b
        right = a % b
        gcd(left, right)
    else:
        print('最大公因數是'+str(b))



one = int(input('請輸入第一個數字'))
two = int(input('請輸入第二個數字'))

gcd(one, two)
