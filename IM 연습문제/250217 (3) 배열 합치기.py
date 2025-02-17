import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    if len(A) < len(B):
        big_arr = B
    else:
        big_arr = A

    for i in range(len(big_arr)):
        if i < N and i < M:
            C.append(A[i])
            C.append(B[i])
        elif N < M:
            C.append(B[i])
        else:
            C.append(A[i])
    print(f'#{tc}', *C)






# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     C = [0] * (N+M)
#     i =0
#     j=0
#
#     while i + j < (N + M):
#         if i < N:
#             C[i + j] = A[i]
#             i += 1
#         if j < M:
#             C[i + j] = B[j]
#             j += 1
#     print(f'#{tc}', *C)
