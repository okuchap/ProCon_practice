def find_gcd(a, b):
    '''
    a >= b
    '''
    if a % b == 0:
        return b
    else:
        return find_gcd(b, a % b)


li = list(map(int, input().split()))

a = max(li)
b = min(li)

div = find_gcd(a, b)
print(div)
