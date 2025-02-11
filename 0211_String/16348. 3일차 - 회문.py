import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() * N for _ in range(N)]
    # print(arr)
    for i in range(N):
        for j in range(N - M + 1):
            s = arr[i][j: j + M]
            if s == s[::-1]:
                print(f'#{tc} {s}')

    for i in range(N):
        for j in range(N - M + 1):
            s = ''.join(arr[j + k][i] for k in range(M))
            if s == s[::-1]:
                print(f'#{tc} {s}')

