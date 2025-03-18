import sys
sys.stdin = open('input.txt', 'r')

def success_work(cnt, max_percet):
    global max_percent
    remaining_max = 1
    for i in range(cnt, N):
        remaining_max *= max_v[i]
    if max_percent * remaining_max <=

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100
    max_v = [max(row) for row in arr]
    visited = [0] * N

    max_percent = 0
    success_work(0, 1)

    print(f'#{tc}', '{:6f}'.format(answer))