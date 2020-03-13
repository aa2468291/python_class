a = int(input('請輸入邊長a，且a<b<c'))
b = int(input('請輸入邊長b，且a<b<c'))
c = int(input('請輸入邊長c，且a<b<c'))

if a + b > c:
    if a * a + b * b > c * c:
        if a == b and b == c:
            print('正三角形')
        elif a == b or b == c:
            print('等腰銳角三角形')
        else:
            print('銳角三角形')

    elif a * a + b * b == c * c:
        if a == b:
            print('等腰直角三角形')
        else:
            print('直角三角形')
    else:
        if a == b:
            print('等腰鈍角三角形')
        else:
            print('鈍角三角形')

else:
    print('不能成為三角形')
