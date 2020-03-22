n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0

for i in range(q):
    q_temp = T[i]
    S.append(q_temp)
    j = 0
    while S[j] != q_temp:
        j += 1
    if j < n:
        ans += 1

print(ans)
