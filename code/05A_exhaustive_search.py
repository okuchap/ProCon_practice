n = int(input())
li_in = list(map(int, input().split()))
q = int(input())
li_check = list(map(int, input().split()))

ubd = 2000

table = [False] * (ubd + 5)
S = [0] * n


def enum(i):
    global table
    if i == n:
        sum = 0
        for j in range(n):
            sum += li_in[j] * S[j]
        if sum <= 2000:
            table[sum] = True
    else:
        enum(i + 1)
        S[i] = 1
        enum(i + 1)
        S[i] = 0


enum(0)

for val in li_check:
    if table[val]:
        print('yes')
    else:
        print('no')


# 失敗作: 毎回再帰で計算
# 各回，数が一つくるごとに全探索している．
# 時間がかかりすぎる．最初に可能な数を全て計算した上でストックし，それを各数に対して用いれば良い．

# S = [0] * n
# flag = False


# def enum(i, val):
#     global flag
#     if i == n:
#         sum = 0
#         for j in range(n):
#             sum += li_in[j] * S[j]
#         if sum == val:
#             flag = True
#     else:
#         enum(i + 1, val)
#         S[i] = 1
#         enum(i + 1, val)
#         S[i] = 0


# for val in li_check:
#     flag = 0
#     enum(0, val)
#     if flag:
#         print('yes')
#     else:
#         print('no')
