# import sys
#
# sys.stdin = open('input.txt', 'r')
from heapq import heappop, heappush


def dijkstra(start):
    heap = []

    heappush(heap, (0, start))
    D[start] = 0

    while heap:
        w, v = heappop(heap)
        if w > D[v]:
            continue

        for t, t_w in g[v]:
            new_distance = w + t_w
            if new_distance < D[t]:
                D[t] = new_distance
                heappush(heap, (new_distance, t))


T = int(input())
for tc in range(1, T + 1):
    # N: 마지막 연결지점 번호, E: 도로의 개수
    N, E = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    INF = int(10e9)
    D = [INF] * (N + 1)

    # E번 반복
    for i in range(E):
        # s: 구간 시작, e: 구간의 끝 지점, w: 구간 거리
        s, e, w = map(int, input().split())
        g[s].append((e, w))

    dijkstra(0)
    print(f'#{tc} {D[N]}')
