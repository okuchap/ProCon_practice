n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0

# 再帰で書くと遅い

# def bin_search(li_sorted, val):
#     global ans
#     m = len(li_sorted)
#     l = int(m / 2)
#     if val == li_sorted[l]:
#         ans += 1
#     elif m > 1:
#         li_left = li_sorted[:l]
#         li_right = li_sorted[l:]
#         bin_search(li_left, val)
#         bin_search(li_right, val)


# for i in range(q):
#     bin_search(S, T[i])

for i in range(q):
    val = T[i]
    left = 0
    right = n
    while left < right:
        mid = (left + right)//2
        if S[mid] == val:
            ans += 1
            break
        elif S[mid] < val:
            left = mid + 1
        else:
            right = mid

print(ans)
