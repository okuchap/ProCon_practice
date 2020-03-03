from math import sqrt

li = []
N = int(input())
for _ in range(N):
    li.append(int(input()))

# li = [5, 2, 3, 4, 5, 6]
li = set(li)

count = 0
for v in li:
    if v == 2:
        count += 1
    elif v % 2 == 0:
        continue
    else:
        ubd = int(sqrt(v))
        flag = 1
        for i in range(3, ubd+1):
            if v % i == 0:
                flag = 0
                break
        count += flag

print(count)
