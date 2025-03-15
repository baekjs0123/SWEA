# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    # print(A, B, C)
    if B < 2 or C < 3:
        print(f'#{tc} -1')
        continue
    cnt = 0

    if B >= C:
        cnt += B - (C - 1)
        B = C - 1
    if A >= B:
        cnt += A - (B - 1)
        A = B - 1
    print(f'#{tc} {cnt}')
