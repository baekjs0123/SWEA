import sys
sys.stdin = open('input.txt', 'r')

def min_cost(cnt, val):
    global min_v

    if val >= min_v:
        return

    if cnt == N:
        min_v = min(min_v, val)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            min_cost(cnt + 1, val + production_cost[cnt][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    production_cost = [list(map(int, input().split())) for _ in range(N)]

    min_v = 1500
    visited = [0] * N
    min_cost(0, 0)
    print(f'#{tc} {min_v}')