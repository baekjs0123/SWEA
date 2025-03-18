import sys

sys.stdin = open('input.txt', 'r')

def success_work(cnt, percent):
    global max_percent
    remaining_max = 1
    for i in range(cnt, N):
        remaining_max *= max_v[i]
    if percent * remaining_max <= max_percent:
        return
    if percent <= max_percent:
        return

    if cnt == N:
        max_percent = max(max_percent,percent)
        return

    for i in range(N):
        if not visited[i] and arr[cnt][i] > 0:
            visited[i] = 1
            success_work(cnt + 1, percent * arr[cnt][i])
            visited[i] = 0

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
    result = max_percent * 100
    print(f'#{tc} {result:.6f}')